from django.contrib import admin
from .models import Evaluation, Subject

class EvaluationInline(admin.TabularInline):
    model = Evaluation
    extra = 0
    list_display = (
        'subject',
        'description',
        'understand',
        'not_yet',
        'student',
    )

class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'published_date',
        'author',
    )
    inlines = [EvaluationInline]

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Evaluation)
