from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/', views.todo, name='todo'),
    path('create/', views.create, name='create'),
    path('todo/<int:id>', views.todo_view, name='todo_view'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]