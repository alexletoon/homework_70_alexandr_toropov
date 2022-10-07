from django.urls import path



from task_app.views.base import IndexView, DetailView, AddView

urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path("task/<int:pk>", DetailView.as_view(), name='task_view'),
    path('add_task/', AddView.as_view(), name='add_task')
] 