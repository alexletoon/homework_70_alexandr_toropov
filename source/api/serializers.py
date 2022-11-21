from rest_framework import serializers
from task_app.models.project import Project
from task_app.models.task import Task


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'description', 'start_date', 'finish_date', 'created_at', 'changed_at', 'user')
        read_only_fields = ('user',)


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'project', 'task', 'description', 'status', 'type', 'created_at', 'changed_at')
        read_only_fields = ('status', 'type', 'project')