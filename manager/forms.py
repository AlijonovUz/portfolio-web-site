from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['portfolio']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'lastname': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control"
            }),
            'text': forms.Textarea(attrs={
                'class': "form-control",
                'rows': 3
            })
        }
