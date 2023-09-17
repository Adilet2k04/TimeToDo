from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_task, name='add_task'),
    path('update_status/<int:task_id>', update_status_task, name='update_status'),
    path('edit_task/<int:task_id>', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>', delete_task, name='delete_task'),
    path('register/', register, name='register')
]