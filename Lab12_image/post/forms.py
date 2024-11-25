from django import forms
from . models import Post
class PostForm(forms, ModelsForm):
    class Meta:
        model = Postfields = ['title', image]