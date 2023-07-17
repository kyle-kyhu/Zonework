from django.contrib import admin
from .models import Student, Subject, Session


class SessionInline(admin.TabularInline):
    model = Session


class SubjectAdmin(admin.ModelAdmin):
    inlines = [
        SessionInline,
    ]
    list_display = [
        "enter_subject",
        "student",
        "subject_date",
    ]


admin.site.register(Student)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Session)
