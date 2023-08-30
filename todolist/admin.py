from django.contrib import admin
from .models import Task
from .models import AdvUser

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'author', 'pub_date', 'is_active')
    fields = (('title', 'author'), 'description', 'category')


admin.site.register(Task, TaskAdmin)
# admin.site.register(AdvUser)
