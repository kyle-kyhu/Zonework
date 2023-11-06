from django import forms

from .models import Assessment, SubAssessment, Evaluation

ASSESSMENT_CHOICES= [
    ('understood', 'Understood'),
    ('not yet', 'Not Yet'),
    ]

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = '__all__'

class SubAssessmentForm(forms.ModelForm):
    class Meta:
        model = SubAssessment
        fields = ("assessment", "notes")                  
        widgets = {
            "assessment": forms.RadioSelect(choices=ASSESSMENT_CHOICES)
        }

# class SecondAssessmentForm(forms.Form):
#     choice = [('understand', 'Understand'), ('not_yet', 'Not Yet')]
#     widget = forms.RadioSelect(choices=choice)
#     notes = forms.CharField(max_length=255)

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ["understand", "not_yet", "notes"]
        widgets = {
            "notes": forms.Textarea(attrs={'placeholder': 'Enter Description', 'style': 'width: 100%','rows': 3}),
        }