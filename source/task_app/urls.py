from django.urls import path



from task_app.views.base import IndexView, DetailView, AddView, TaskUpdateView, DeleteTask
from task_app.views.project import ProjectListView, ProjectDetailView, ProjectCreateView, UpdateProjectView

urlpatterns = [
    path("", ProjectListView.as_view(), name='index_view'),
    path("task/<int:pk>", DetailView.as_view(), name='task_view'),
    path('add_task/<int:pk>', AddView.as_view(), name='add_task'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='update_task'),
    path('delete_task/<int:pk>', DeleteTask.as_view(), name='delete_task'),
    path('projects_list/', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('add_project/', ProjectCreateView.as_view(), name='add_project'),
    # path('project/<int:pk>/add_user/', UpdateProjectView.as_view(), name='add_user'),
    path('update_project/<int:pk>', UpdateProjectView.as_view(), name='add_user'), 
] 