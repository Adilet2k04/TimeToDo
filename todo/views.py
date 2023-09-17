from django.shortcuts import render, get_object_or_404, redirect
from .services import *
from .forms import *


def home(request):
    return render(request, 'todo/home.html', context={'title': 'Homepage', 'all_tasks': get_all_objects_from_todo_db()})


def add_task(request):
    form = TaskAddForm(request.POST)
    if form.is_valid():
        task_title = form.cleaned_data['task_title']
        task_content = form.cleaned_data['task_content']
        task_category = form.cleaned_data['task_category']
        add_task_to_db(task_title, task_content, task_category)
        return redirect('home')
    return render(request, 'todo/add_task.html', {'form': form})


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskEditForm(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data['new_title']
            new_content = form.cleaned_data['new_content']
            new_category = form.cleaned_data['new_category']
            new_due_date = form.cleaned_data['new_due_date']
            edit_title_and_content_of_the_task(task_id, new_title, new_content, new_category, new_due_date)
            return redirect('home')
    else:
        form = TaskEditForm(initial={'new_title': task.task_title,
                                     'new_content': task.task_content,
                                     'new_category': task.task_category,
                                     'new_due_date': task.task_due_date})
    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})


def update_status_task(request, task_id):
    update_status_of_the_task(task_id)
    return redirect('home')


def delete_task(request, task_id):
    delete_task_from_db(task_id)
    return redirect('home')


def register(request):
    pass



