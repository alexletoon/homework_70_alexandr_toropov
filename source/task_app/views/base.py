from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, UpdateView, DeleteView, ListView, CreateView
from task_app.forms import SearchForm
from task_app.models.task import Task
from task_app.models.project import Project
from task_app.forms import TaskForm
import datetime
from datetime import timedelta
from django.utils.timezone import utc
from django.utils.http import urlencode
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin





now = datetime.datetime.utcnow().replace(tzinfo=utc)

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = ['-created_at']
    paginate_by: int = 3
    paginate_orphans: int = 1


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

class AddView(LoginRequiredMixin, CreateView):
    template_name: str = 'add_task.html'
    model = Task
    form_class = TaskForm
    success_url = '/'


    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     return super(AddView, self ).dispatch(request, *args, **kwargs)
        


    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = '/'


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name: str = 'confirm_delete.html'
    success_url = '/'
