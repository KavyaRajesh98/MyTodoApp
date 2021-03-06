from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),
    path('complete/<todo_id>', views.completedTodo, name='complete'),
    path('deleteCompleted', views.deleteCompleted, name='deleteCompleted'),
    path('deleteall', views.deleteAll, name='deleteall')
]
