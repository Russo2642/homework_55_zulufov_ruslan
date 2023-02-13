from django.contrib import admin

from webapp.models import ToDo


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'completion_at')
    list_filter = ('id', 'description', 'status', 'completion_at')
    search_fields = ('id', 'description')
    fields = ('description', 'status', 'completion_at')
    readonly_fields = ('id', 'completion_at')


admin.site.register(ToDo, ToDoAdmin)
