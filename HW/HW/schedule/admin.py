from django.contrib import admin
from .models import Exam, Group, Schedule


class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'lecturer')
    search_fields = ('name', 'lecturer')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('group', 'lesson', 'lesson_time', 'consultation_time')


admin.site.register(Exam, ExamAdmin)
admin.site.register(Group)
admin.site.register(Schedule, ScheduleAdmin)
