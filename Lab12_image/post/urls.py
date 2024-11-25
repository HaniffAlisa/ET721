from . views import HomePageView, CreatePostView

urlpatterns =[
    path('', HomePageView(), name = 'home'),
    path('post', CreatePostView(), name='add_post),
    
]