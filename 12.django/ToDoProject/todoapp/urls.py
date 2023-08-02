from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/', views.todo, name='todo'),
    path('create/', views.create, name='create'),
    path('<int:id>', views.todo_view, name='todo_view'), # todo/<int:id> todo 생략 가능
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete')
]

# 현재 
# todo/create
# todo/<tid>/
# todo/<tid>/update
# todo/<tid>/delete

# todo/<tid>/  method:CRUD 이런식의 url이어야 함
# method == delete 이런식으로 받아서 처리
# 결과적으로 path로 todo/, todo/<int:id>만 남아 있어야 함
