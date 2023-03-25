from django.db.models import Q
from .models import Record, Topic
from .forms import RecordForm

from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache

from .models import Record


# Страница подтверждения записи
@never_cache
def appointment_approve(request):
    return render(request, 'thanks.html', {'text': 'Ваша запись зарегистрирована'})


@never_cache
def create_student(request, *args, **kwargs):
    form = RecordForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        selected_topic = form.cleaned_data['topic_title']  # берем значение темы из формы
        if form.is_valid():
            # обновляем значение reserved_status у темы после отправки
            Topic.objects.filter(title=selected_topic).update(reserved_status=True)
            form.save()  # сохраняем форму
            return redirect('appointment_approve')
    else:
        form = RecordForm()
    return render(request, 'create_record.html', {'form': form})