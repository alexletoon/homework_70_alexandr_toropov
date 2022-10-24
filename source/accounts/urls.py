from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView



from task_app.views.base import IndexView, DetailView, AddView, TaskUpdateView, DeleteTask
from task_app.views.project import ProjectListView, ProjectDetailView, ProjectCreateView

urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", logout_view, name='logout'),
    path("register/", RegisterView.as_view(), name='register'),
]