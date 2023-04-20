from django import forms
from .models import LearningItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = LearningItem
        fields = [
            "title",
            'completed',
            'description',
            'entry_date'
        ]

