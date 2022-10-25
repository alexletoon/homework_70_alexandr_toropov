from urllib import request
from django.views.generic import UpdateView, DeleteView, ListView, DetailView, CreateView
from task_app.models.project import Project
from task_app.forms import ProjectForm, AddUserForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

class ProjectListView(ListView):
    template_name = 'projects_list.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['-created_at']
    paginate_by: int = 5
    paginate_orphans: int = 1


    def get_queryset(self):
        if self.request.user.is_superuser or not self.request.user.is_authenticated:
            return super().get_queryset()
        # elif not self.request.user.is_authenticated
        return super().get_queryset().filter(user__username=self.request.user)


class ProjectDetailView(UserPassesTestMixin, DetailView):
    template_name: str = 'project_detail.html'
    model = Project


    def test_func(self):
        return self.request.user.is_superuser or self.request.user in self.get_object().user.all() and self.request.user.has_perm('task_app.view_project')
 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.tasks.order_by('created_at')
        context['tasks']: tasks
        return context


class ProjectCreateView(UserPassesTestMixin, CreateView):
    template_name: str = 'project_add.html'
    model = Project
    form_class = ProjectForm


    def test_func(self):
        return self.request.user.has_perm('task_app.add_project')


    def get_success_url(self) -> str:
        return reverse('project_list')
    


class AddUserProjectView(UserPassesTestMixin, UpdateView):
    model = Project
    form_class = AddUserForm
    template_name: str = 'add_user.html'
    success_url = '/'

    def test_func(self):
            return self.request.user.is_superuser or  self.request.user in self.get_object().user.all() and self.request.user.has_perm('task_app.change_project')

    def get(self, request, *args, **kwargs):
        print(self.kwargs.get('pk'))
        return super().get(request, *args, **kwargs)
    

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class UpdateProjectView(UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name: str = 'update_project.html'
    success_url = '/'

    def test_func(self):
            return self.request.user.is_superuser or  self.request.user in self.get_object().user.all() and self.request.user.has_perm('task_app.change_project')

    def get(self, request, *args, **kwargs):
        print(self.kwargs.get('pk'))
        return super().get(request, *args, **kwargs)
    

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class DeleteProjectView(UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'confirm_project_delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser or  self.request.user in self.get_object().user.all() and self.request.user.has_perm('task_app.delete_project')

