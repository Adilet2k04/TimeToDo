from .models import *
from django.utils import timezone


def get_all_objects_from_todo_db():
    return Task.objects.all()


def add_task_to_db(task_title, task_content, task_category=None):
    task = Task(task_title=task_title,
                task_content=task_content,
                task_category=task_category)
    task.save()


def edit_title_and_content_of_the_task(task_id, new_title='', new_content='', new_category=None, new_due_date=None):
    time = timezone.now()
    task = Task.objects.get(id=task_id)
    if len(new_title) > 0:
        task.task_title = new_title
    if len(new_content) > 0:
        task.task_content = new_content
    if new_category:
        task.task_category = new_category
    if new_due_date > time:
        task.task_due_date = new_due_date
    task.save()


def update_status_of_the_task(task_id):
    task = Task.objects.get(id=task_id)
    task.task_is_complete = not task.task_is_complete
    task.save()


def delete_task_from_db(task_id):
    task = Task.objects.get(id=task_id)
    task.delete()


