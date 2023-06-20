from django import forms
from .models import LearningItem

class ItemForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'style': 'width: 200px; height: 50px;'})
    )
    class Meta:
        model = LearningItem
        fields = [
            'student',
            'completed',
            'title',
            'entry_date'
        ]


def MyLearningItem():
    # this is a dummy object to test the form
    # learning_items = [{'subject': 'Maths', 'assessment': 'Assessment 1', 'description': 'Description 1'},
    #                   {'subject': 'English', 'assessment': 'Assessment 2', 'description': 'Description 2'},
    # ]
    #return learning_items
    pass