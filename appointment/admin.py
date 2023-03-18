from django.contrib import admin
from .models import Record, Supervisor, Topic


class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree')
    list_filter = ('name', 'degree')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'reserved_status')
    list_filter = ('title', 'supervisor', 'reserved_status')


class RecordAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'topic_title', 'supervisor_name')
    list_filter = ('student_name', 'topic_title__title', 'supervisor_name__name')
    search_fields = ('student_name', 'topic_title__title', 'supervisor_name__name')  # А как сделать поиск по темам и руководителям?


admin.site.register(Record, RecordAdmin)
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(Topic, TopicAdmin)
