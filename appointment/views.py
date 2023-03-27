from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache

from .models import Record, Topic, Archive
from .forms import RecordForm

# Страница подтверждения записи
@never_cache
def appointment_approve(request):
    return render(request, 'thanks.html', {'text': 'Ваша запись зарегистрирована'})
    
@never_cache
def create_student(request, *args, **kwargs):
    form = RecordForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        student_name = form.cleaned_data['student_name']    # берем значение ФИО студента из формы
        selected_topic = form.cleaned_data['topic_title']   # берем значение темы из формы
        supervis_name = form.cleaned_data['supervisor_name'] # берем значение ФИО руководителя из формы
        
        # обновляем значение reserved_status у темы после отправки
        Topic.objects.filter(title=selected_topic).update(reserved_status=True)
        form.save()  # сохраняем форму

        # отправляем данные ещё и в "Архив"
        archive = Archive(name=student_name, supervis_name=supervis_name, top_title=selected_topic)
        archive.save()

        return redirect('appointment_approve')
    else:
        form = RecordForm()
    return render(request, 'create_record.html', {'form': form})
