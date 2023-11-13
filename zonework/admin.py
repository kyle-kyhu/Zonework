from django.contrib import admin
from .models import Subject, Assessment, SubAssessment, Evaluation

class EvalutationInline(admin.TabularInline):
    model = Evaluation
    extra = 0
    list_display = [
        ""
    ]

class AssessmentInline(admin.TabularInline):
    model = Assessment
    extra = 0

class SubAssessmentInline(admin.TabularInline):
    model = SubAssessment
    extra = 0


class SubjectAdmin(admin.ModelAdmin):
    inlines = [
        AssessmentInline,
    ]
    list_display = [
        "title",
        "author",
    ]



admin.site.register(Subject, SubjectAdmin)
admin.site.register(Assessment)
admin.site.register(SubAssessment)
admin.site.register(Evaluation)

