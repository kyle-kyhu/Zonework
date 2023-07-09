from django import forms
from .models import LearningItem


class ItemForm(forms.ModelForm):
    class Meta:
        model = LearningItem
        fields = [
            "completed",
            "subject",
            "text",
        ]
