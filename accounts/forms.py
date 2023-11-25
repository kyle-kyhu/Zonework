from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # CustomUserCreationForm
    # Fields: email, password1, password2
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('is_student', 'is_author')

class CustomUserChangeForm(UserChangeForm):
    # CustomUserChangeForm
    # Fields: email, password
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields