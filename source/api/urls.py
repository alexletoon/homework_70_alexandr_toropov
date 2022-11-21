from django.urls import path

from api.views import TaskDetailView, ProjectDetailView

urlpatterns = [
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project'),
]