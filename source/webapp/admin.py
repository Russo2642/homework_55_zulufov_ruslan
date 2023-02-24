from django.contrib import admin

from webapp.models import ToDo


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'completion_at', 'detailed_description',
                    'is_deleted', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('id', 'title', 'description', 'status', 'completion_at', 'detailed_description',
                    'is_deleted', 'created_at', 'updated_at', 'deleted_at')
    search_fields = ('id', 'title')
    fields = ('title', 'description', 'status', 'completion_at', 'detailed_description')
    readonly_fields = ('id', 'completion_at')


admin.site.register(ToDo, ToDoAdmin)
