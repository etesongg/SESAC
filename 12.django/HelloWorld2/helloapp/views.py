from django.shortcuts import render
from django.http import HttpResponse
from .models import Message


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World')

def show_messages(request):
    # db로 부터 메세지 받아오기 (orm을 사용해서)
    messages = Message.objects.all() 
    print(messages)
    return render(request, 'message_list.html',{'messages': messages})

