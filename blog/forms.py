from django import forms

from djrichtextfield.widgets import RichTextWidget

from .models import Review


class ReviewCreateForm(forms.ModelForm):
    # post = forms.CharField(widget=RichTextWidget())

    class Meta:
        model = Review
        fields = ['title', 'post']