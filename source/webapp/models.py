from django.db import models
from django.utils import timezone


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Наименование")
    description = models.CharField(max_length=300, null=False, blank=False, help_text="Опишите задачу",
                                   verbose_name="Описание")
    status = models.CharField(max_length=200, null=False, blank=False, default="new", verbose_name="Статус")
    completion_at = models.CharField(max_length=50, null=True, verbose_name="Дата дедлайна")
    detailed_description = models.TextField(max_length=3000, null=True, verbose_name="Детальное описание")
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    deleted_at = models.DateTimeField(verbose_name="Дата и время удаления", null=True, default=None)

    def __str__(self):
        return f"{self.title} - {self.status}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'
