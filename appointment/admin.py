from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import Record, Supervisor, Topic

# миксин для экспорта csv
class ExportCsvMixin:
    def export_as_csv(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        
        opts = self.model._meta

        response = HttpResponse(content_type='text/csv')
        # принудительное скачивание
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts)
        response.write(u'\ufeff'.encode('utf8'))
        header = [field.name for field in opts.fields]
        writer = csv.DictWriter(response, fieldnames=header)
        # Вносим шапку в файл
        writer.writeheader()

        # получить все записи
        records = Record.objects.all()

        # Вносим данные в файл
        for obj in records:
            writer.writerow(
                {
                    "id": obj.id,
                    "student_name": obj.student_name,
                    "supervisor_name": obj.supervisor_name,
                    "topic_title": obj.topic_title,
                }
            )

        return response

    export_as_csv.short_description = "Экспорт в csv"

class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree')
    list_filter = ('name', 'degree')
    search_fields = ('name', )


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'reserved_status')
    list_filter = ('title', 'supervisor__name', 'reserved_status')
    search_fields = ('title', 'supervisor__name')


class RecordAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('student_name', 'topic_title', 'supervisor_name')
    list_filter = ('student_name', 'topic_title__title', 'supervisor_name__name')
    search_fields = ('student_name', 'topic_title__title', 'supervisor_name__name')  # А как сделать поиск по темам и руководителям?
    actions = ["export_as_csv"]

admin.site.register(Record, RecordAdmin)
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(Topic, TopicAdmin)