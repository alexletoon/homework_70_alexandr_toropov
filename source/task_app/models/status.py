from django.db import models


class Status(models.Model):
    status = models.CharField(verbose_name='Статус', max_length=50, null=False, blank=False)


    def __str__(self) -> str:
        return f'Status - {self.status}'