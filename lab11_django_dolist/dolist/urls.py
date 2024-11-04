from django.urls import path
from . import views # . means import from the same directory
urlpatterns = [
#load page of the app will be sent to the 'index.html' file
path('', views.index, name='index'),
]