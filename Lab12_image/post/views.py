from django.shortcuts import render
from django.views.generic import ListViews, CreateView
from django.urls import reverse_lazy
from . forms import PostForm
from . models import Post

# Create your views here.
class HomePageView(ListView):
    model =Posttemplate_name = 'home.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url =reverse_lazy('home')    