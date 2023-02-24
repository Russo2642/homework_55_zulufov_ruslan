from django import forms
from django.core.exceptions import ValidationError

from webapp.models import ToDo

STATUS_CHOICES = [
    ('new', 'New'),
    ('in process', 'In Process'),
    ('done', 'Done')
]


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'description', 'status', 'completion_at', 'detailed_description')
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'completion_at': 'Дедлайн',
            'detailed_description': 'Подробное описание'
        }
        widgets = {
            'status': forms.Select(choices=STATUS_CHOICES),
            'completion_at': forms.SelectDateWidget(empty_label="Nothing")
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее 2 символов')
        return title
