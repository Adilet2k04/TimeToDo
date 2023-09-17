from django import forms
from .models import *


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class TaskEditForm(forms.Form):
    new_title = forms.CharField(max_length=100, required=False)
    new_content = forms.CharField(widget=forms.Textarea, required=False)
    new_category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select category")
    new_due_date = forms.DateTimeField()


class TaskAddForm(forms.Form):
    task_title = forms.CharField(max_length=100)
    task_content = forms.CharField(widget=forms.Textarea, required=False)
    task_category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select category")




