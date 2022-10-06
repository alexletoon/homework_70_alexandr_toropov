from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from task_app.models.task import Task


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
        return super().get_context_data(**kwargs)
        # add_form = AddForm()
        # if add_form.is_valid():
        #     context['task'] = 