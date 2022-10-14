from django.views.generic import TemplateView, UpdateView, DeleteView, ListView, DetailView, CreateView
from task_app.models.project import Project
from task_app.forms import ProjectForm


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


class ProjectCreateView(CreateView):
    template_name: str = 'project_add.html'
    model = Project
    form_class = ProjectForm
    success_url = '/'
