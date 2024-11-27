from django import forms
from . models import Post

class PostForm(forms.ModeForm):
    class Meta:
        model =Postfields =['title', 'image']