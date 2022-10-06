from django.db import models


class Type(models.Model):
    type = models.CharField(verbose_name='Тип задания', max_length=50, null=False, blank=False)


    def __str__(self) -> str:
        return f'Type - {self.type}'