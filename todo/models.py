from django.db import models
from django.utils import timezone


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_time_create = models.DateTimeField(auto_now_add=True)
    task_content = models.TextField(blank=True)
    task_is_complete = models.BooleanField('Completed', default=False)
    task_due_date = models.DateTimeField(default=one_week_hence)
    task_category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.task_title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'








