from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company


class MyCustomSignupForm(UserCreationForm):
    company = forms.ChoiceField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "company"]
