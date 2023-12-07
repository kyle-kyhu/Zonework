from django import forms

from .models import Evaluation

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = (
            'understand',
            'not_yet',
            'description',
        )
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter your description here',
                    'style': 'height: 100px', 
                    'rows': 3,
                    }),
        }