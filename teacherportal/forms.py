from django import forms
from .models import Teacher

class LoginForm(forms.Form):
    username = forms.CharField(label="Teacher Email", help_text="e.g 1-joshua-kalule")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Teacher
        fields = ["email", "first_name", "last_name", "age", "password", "subject_name", "class_name"]

