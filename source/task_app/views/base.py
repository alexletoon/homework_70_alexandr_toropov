from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, UpdateView, DeleteView, ListView
from task_app.forms import SearchForm
from task_app.models.task import Task
from task_app.forms import TaskForm
import datetime
from datetime import timedelta
from django.utils.timezone import utc
from django.utils.http import urlencode
from django.db.models import Q



now = datetime.datetime.utcnow().replace(tzinfo=utc)

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = ['-created_at']
    paginate_by: int = 3
    paginate_orphans: int = 1
    # allow_empty: bool = False


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context
    

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(task__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset
    

    def get_search_form(self):
        return SearchForm(self.request.GET)

    
    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


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
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = '/'


class DeleteTask(DeleteView):
    model = Task
    template_name: str = 'confirm_delete.html'
    success_url = '/'
