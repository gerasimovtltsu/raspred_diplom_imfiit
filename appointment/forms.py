from django import forms
from .models import Record, Topic


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['student_name', 'supervisor_name', 'topic_title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # задаем стили для полей
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'