from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_title', 'task_time_create']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
