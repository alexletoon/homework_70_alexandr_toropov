from django.db import models


class Project(models.Model):
    project = models.CharField(verbose_name='Имя проекта', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=2000, null=False, blank=False)
    start_date = models.DateField(verbose_name='Дата старта', null=False, blank=False)
    finish_date = models.DateField(verbose_name='Дата завершения', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)


    def __str__(self) -> str:
        return f'Project - {self.project}, Description - {self.description}, start_date = {self.start_date}'


    def get_tasks(self):
        if self.tasks:
            return self.tasks.order_by('created_at')