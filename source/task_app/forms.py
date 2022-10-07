from django import forms
from django.forms import widgets 
from task_app.models.status import Status
from task_app.models.type import Type



class TaskForm(forms.Form):
    task = forms.CharField(max_length=200, required=True, label='Задача')
    description = forms.CharField(max_length=2000, required=False, label='Описание', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус', widget=widgets.RadioSelect)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Тип задачи', widget=widgets.RadioSelect)
