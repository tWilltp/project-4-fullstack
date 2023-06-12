from .models import ReviewComments
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = ReviewComments
        fields = ('body',)
