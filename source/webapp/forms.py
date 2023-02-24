from django import forms
from django.core.exceptions import ValidationError


class ToDoForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Заголовок')
    text = forms.CharField(max_length=3000, required=True, label='Текст')
    status = forms.CharField(max_length=200, required=True, label='Статус')
    completion_at = forms.DateField(required=True, label='Дедлайн')
    detailed_description = forms.CharField(max_length=3000, required=False, label='Детальное описание')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее 2 символов')
        return title
