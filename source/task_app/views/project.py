from django.views.generic import TemplateView, UpdateView, DeleteView, ListView, DetailView, CreateView
from task_app.models.project import Project
from task_app.forms import ProjectForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectListView(ListView):
    template_name = 'projects_list.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['-created_at']
    paginate_by: int = 3
    paginate_orphans: int = 1


class ProjectDetailView(DetailView):
    template_name: str = 'project_detail.html'
    model = Project


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.tasks.order_by('created_at')
        context['tasks']: tasks
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name: str = 'project_add.html'
    model = Project
    form_class = ProjectForm
    # success_url = '/'

    def get_success_url(self) -> str:
        return reverse('project_list')

    
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('login')
    #     return super(ProjectCreateView, self ).dispatch(request, *args, **kwargs)
