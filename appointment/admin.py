from django.contrib import admin
from .models import Record, Student, Supervisor, Topic


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group', )
    search_fields = ('name', 'group')


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree')
    list_filter = ('name', 'degree')
    search_fields = ('name', 'degree')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'reserved_status')
    list_filter = ('title', 'supervisor', 'reserved_status')
    search_fields = ('title', 'supervisor')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'topic_title', 'supervisor_name')
    list_filter = ('student_name', 'topic_title', 'supervisor_name')
    search_fields = ('student_name', 'topic_title', 'supervisor_name')
