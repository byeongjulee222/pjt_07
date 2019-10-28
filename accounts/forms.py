from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')
        