from django.urls import path
from . import views 

urlpatterns = [
    #load page of the app will be sent to th 'index.html' file
    path( "", views.index, name='index')
]