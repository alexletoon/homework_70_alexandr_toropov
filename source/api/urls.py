from django.urls import path

from api.views import TaskDetailView

urlpatterns = [
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='article')
]