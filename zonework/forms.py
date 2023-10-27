from django import forms

from .models import Assessment, SubAssessment


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ("assessment","notes")

class SubAssessmentForm(forms.ModelForm):
    class Meta:
        model = SubAssessment
        fields = ("assessment", "notes")                  
        widgets = [('understand', 'Understand'), ('not_yet', 'Not Yet')]
    

