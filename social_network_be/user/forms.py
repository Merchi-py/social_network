from django import forms

from .models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["avatar", "username"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form_control"
            }),
            "first_name": forms.Textarea(attrs={
                "class": "form_control"
            }),
            "last_name": forms.Textarea(attrs={
                "class": "form_control"
            })
        }