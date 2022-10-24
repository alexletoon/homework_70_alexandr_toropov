from django import forms
from django.forms import ModelForm, SelectDateWidget, widgets, MultipleChoiceField
from django.forms.widgets import DateInput
from task_app.models.status import Status
from task_app.models.task import Task
from task_app.models.project import Project
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



def title_length_validator(string):
    if len(string) > 20 or len(string) < 3:
        raise ValidationError('Данная строка должна быть не менее 3х символов, но не более 20')
    return string 


class TaskForm(forms.ModelForm):
    task = forms.CharField(max_length=200, required=True, label='Задача', validators=(title_length_validator,))
    description = forms.CharField(max_length=2000, required=False, label='Описание', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус', widget=widgets.RadioSelect)

    class Meta:
        model = Task
        fields = ['task', 'description', 'status', 'type']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['project', 'description','start_date', 'finish_date', 'user']
        widgets = {
            'start_date': SelectDateWidget(),
            'finish_date': SelectDateWidget()
        }


class AddUserForm(forms.ModelForm):
    # user = forms.CharField(required=False, label='Пользователи', widget=forms.RadioSelect)
    class Meta:
        model = Project
        fields = ['user']
