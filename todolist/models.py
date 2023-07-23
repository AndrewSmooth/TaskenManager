from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=40, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    category = models.SmallIntegerField(verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, db_index = True, verbose_name='Дата и время публикации')
    is_active = models.BooleanField(default=False, db_index=True, verbose_name = 'Выполнено?')

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['-pub_date']
