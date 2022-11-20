from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from task_app.models.task import Task
from api.serializers import TaskSerializer


class TaskDetailView(APIView):
    def get(request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        serializer = TaskSerializer(task)
        return Response(serializer.data)
