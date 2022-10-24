from django.views.generic import UpdateView, DeleteView, ListView, DetailView, CreateView
from task_app.models.project import Project
from task_app.forms import ProjectForm, AddUserForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

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


    def get_success_url(self) -> str:
        return reverse('project_list')


class UpdateProjectView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = AddUserForm
    template_name: str = 'add_user.html'
    success_url = '/'


    def get(self, request, *args, **kwargs):
        print(self.kwargs.get('pk'))
        return super().get(request, *args, **kwargs)
    

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})

