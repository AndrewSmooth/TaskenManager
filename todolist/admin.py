from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'author', 'pub_date', 'is_active')
    fields = (('title', 'author'), 'description', 'category')

admin.site.register(Task, TaskAdmin)