from django.contrib import admin
from .models import Subject, Assessment


class AssessmentInline(admin.TabularInline):
    model = Assessment
    extra = 0


class SubjectAdmin(admin.ModelAdmin):
    inlines = [
        AssessmentInline,
    ]
    list_display = [
        "title",
        "student",
    ]


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Assessment)
