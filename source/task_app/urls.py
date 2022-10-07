from django.urls import path



from task_app.views.base import IndexView, DetailView, AddView, TaskUpdateView, DeleteTask

urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path("task/<int:pk>", DetailView.as_view(), name='task_view'),
    path('add_task/', AddView.as_view(), name='add_task'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='update_task'),
    path('delete_task/<int:pk>', DeleteTask.as_view(), name='delete_task'),
] 