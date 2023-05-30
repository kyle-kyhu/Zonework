from django import forms
from .models import LearningItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = LearningItem
        fields = [
            'subject',
            'assessment',
            'description',
            #'entry_date'
        ]

def MyLearningItem():
    # this is a dummy object to test the form
    # learning_items = [{'subject': 'Maths', 'assessment': 'Assessment 1', 'description': 'Description 1'},
    #                   {'subject': 'English', 'assessment': 'Assessment 2', 'description': 'Description 2'},
    # ]
    #return learning_items
    pass