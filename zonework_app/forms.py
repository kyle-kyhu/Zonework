from django import forms
from .models import LearningItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = LearningItem
        fields = [
            "subject",
            'assessment',
            'description',
            'entry_date'
        ]
