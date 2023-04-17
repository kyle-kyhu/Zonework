from django import forms
from .models import LearningItem, Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = LearningItem
        fields = [
            "title",
            "in_class",
        ]

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "description",
            "completed",
            "entry_date",
            "student",
            ]