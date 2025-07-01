from django import forms
from .models import Student

class LoginForm(forms.Form):
    username = forms.CharField(label="User ID", help_text="e.g 1-joshua-kalule")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "age", "class_name", "password"]

