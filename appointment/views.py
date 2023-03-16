from django.shortcuts import redirect, render
from .forms import RecordForm


# Страница подтверждения записи
def appointment_approve(request):
    return render(request, 'thanks.html', {'text': 'Ваша запись зарегистрирована'})


def create_student(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_approve')
    else:
        form = RecordForm()
    return render(request, 'create_record.html', {'form': form})
