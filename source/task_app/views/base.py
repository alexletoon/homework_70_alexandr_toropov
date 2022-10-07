from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from task_app.models.task import Task
from task_app.forms import TaskForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class DetailView(TemplateView):
    template_name: str = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class AddView(TemplateView):
    template_name: str = 'add_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TaskForm()
        context['form'] = form
        return context

    
    def post(self, request, *args, **kwargs):
        form = TaskForm(self.request.POST)
        if form.is_valid():
            task = Task.objects.create(**form.cleaned_data)
            return redirect('index_view')
        # add_form = AddForm()
        # if add_form.is_valid():
        #     context['task'] = 