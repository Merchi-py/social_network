from django import forms

from .models import PostModel

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["title", "content", "image"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter the title",
                "class": "form_control"
            }),
            "content": forms.Textarea(attrs={
                "placeholder": "Enter the content",
                "class": "form_control"
            }),
        }

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["title", "content"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter the title",
                "class": "form_control"
            }),
            "content": forms.Textarea(attrs={
                "placeholder": "Enter the content",
                "class": "form_control"
            }),
        }