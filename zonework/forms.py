from django import forms

from .models import Assessment

ASSESSMENT_CHOICES= [
    ('understood', 'Understood'),
    ('not yet', 'Not Yet'),
    ]

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = (
            "assessment",
            "notes",
        )
        widgets = {
            "assessment": forms.Select(choices=ASSESSMENT_CHOICES, attrs={'style': 'width: 300px;', 'class': 'form-control'}),
            "notes": forms.Textarea(attrs={'style': 'width: 300px;', 'class': 'form-control', 'rows': 3}),
        }

