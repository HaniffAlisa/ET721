from django.urls import path
from . import views 

urlpatterns = [
    #load page of the app will be sent to the 'index.html' file
    path("", views.index, name='index'),

    #add new task into list
    path('add', views.addTodoItem, name='add'),

    #mark task as completed
    path('completed/<int:todo_id>/', views.completedTodo, name='completed'),
    
    #delete task that are marked as completed
    path('deletecompleted', views.deletecompleted, name = 'deletecompleted'),

    #delete all tasks
    path('deleteall', views.deleteAll, name='deleteall'),
    
]
