from django.db import models


class Task(models.Model):
    project = models.ForeignKey('task_app.Project', related_name='tasks', on_delete=models.CASCADE, verbose_name='Проект', default=1)
    task = models.CharField(verbose_name='Задача', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=2000, null=False, blank=False)
    status = models.ForeignKey('task_app.Status', verbose_name='Статус', related_name='task', on_delete=models.RESTRICT)
    type = models.ManyToManyField('task_app.Type', verbose_name='Тип задачи', related_name='task')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)


    def __str__(self) -> str:
        return f'Task - {self.task}, Description - {self.description}'
