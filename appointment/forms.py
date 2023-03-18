from django import forms
from .models import Record, Topic


class RecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # переопределение label для полей
        self.fields['student_name'].label = "ФИО студента"
        self.fields['supervisor_name'].label = "ФИО руководителя"
        self.fields['topic_title'].label = "Доступные темы"

        # переопределение help_text для полей
        self.fields['student_name'].help_text = "Введите Ваши ФИО"
        self.fields['supervisor_name'].help_text = "Выберите руководителя из списка"
        self.fields['topic_title'].help_text = "Выберите тему"

        # задаем стили для полей
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input__text'
            visible.field.widget.attrs['placeholder'] = visible.field.help_text

    class Meta:
        model = Record
        fields = ['student_name', 'supervisor_name', 'topic_title']
