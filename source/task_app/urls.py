from django.urls import path



from task_app.views.base import index_view

urlpatterns = [
    path("", index_view)
]