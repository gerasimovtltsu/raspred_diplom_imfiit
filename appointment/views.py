from django.shortcuts import redirect, render
from .forms import RecordForm


def create_student(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_student')
    else:
        form = RecordForm()
    return render(request, 'create_record.html', {'form': form})
