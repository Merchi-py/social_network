from django import forms

from .models import PostTextModel

class PostTextCreationForm(forms.ModelForm):
    class Meta:
        model = PostTextModel
        fields = ["title", "content"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter the title",
                "class": "form_control"
            }),
            "content": forms.Textarea(attrs={
                "placeholder": "Enter the content",
                "class": "form_control"
            })
        }