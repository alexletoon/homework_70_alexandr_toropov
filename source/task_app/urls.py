from django.urls import path



from task_app.views.base import IndexView, DetailView

urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path("task/<int:pk>", DetailView.as_view(), name='task_view'),
] 