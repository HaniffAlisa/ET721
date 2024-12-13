from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'rating']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }