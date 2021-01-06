from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.timezone import localtime
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company


class dateTime(forms.DateInput):
    input_type = 'datetime-local'


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    start_time = forms.DateTimeField(widget=dateTime(), input_formats='%d/%m/%y %H:%M:%S')
    end_time = forms.DateTimeField(widget=dateTime(), input_formats='%d/%m/%y %H:%M:%S')
    # employee = forms.AutoField(primary_key=True, editable=False)

    class Meta:
        model = Post
        fields = '__all__'


class MyCustomSignupForm(UserCreationForm):
    company = forms.ChoiceField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "company"]
