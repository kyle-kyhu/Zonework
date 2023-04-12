from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "description",
            "completed",
            "entry_date",
            "student"
        ]

