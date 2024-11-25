from django.shortcuts import render
from django,views,generic import ListView CreatePostView
from django.urls import reverse_lazy
form .forms import
form .models import Post

# Create your views here.
class HomePageView(ListView):
    model =Post
    template_name = 'home.html'

class CreatePostView(CreateView):
    model = Postform_class = PostForm
    template_name ='post.html'
    success_url= reverse_lazy('home')