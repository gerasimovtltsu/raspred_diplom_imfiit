from django import forms
from .models import Record, Topic


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = 'student_name', 'topic_title', 'supervisor_name'

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

