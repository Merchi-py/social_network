from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

class UserSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password"})
    )

    class Meta:
        model = User
        fields = ["first_name",
        "last_name",
        "username",
        "password1",
        "password2",
        "email"]

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter your first_name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter your last_name"}),
            "username": forms.TextInput(attrs={"placeholder": "Enter your username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your email"}),
        }

class UserSignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter your username"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Enter your password"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your email"}),
        }