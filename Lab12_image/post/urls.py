from . views import HomePageView, CreatePostView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home' ),
    path('post', CreatePostView.as_view(), name = 'add_post'),
]