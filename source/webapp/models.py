from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=3000, null=False, blank=False, help_text="Опишите задачу",
                                   verbose_name="Описание")
    status = models.CharField(max_length=200, null=False, blank=False, default="new", verbose_name="Статус")
    completion_at = models.CharField(max_length=50, null=True, verbose_name="Дата дедлайна")

    def __str__(self):
        return f"{self.title} - {self.status}"
