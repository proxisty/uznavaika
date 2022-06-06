from django import forms
from .models import FeedBackHome


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBackHome
        fields = ['name', 'email', 'phone', 'description']
