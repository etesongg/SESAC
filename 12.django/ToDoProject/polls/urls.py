from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.polls, name='polls'),
    path('polls/<int:ques_id>', views.poll_detail, name='poll_detail'),
    path('poll_result/<int:ques_id>/<int:chois_id>', views.poll_result, name='poll_result')
]