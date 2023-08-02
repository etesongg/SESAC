from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo

# Create your views here.

def home(request):
    return render(request, 'todo/index.html')

def todo(request):
    todos = ToDo.objects.all()
    return render(request, 'todo/todo.html', {'todos' : todos})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        ToDo.objects.create(title=title, description=description)
        return redirect('todo')

    return render(request, 'todo/create.html')

def todo_view(request, id):
    # todo = ToDo.objects.get(id=id)
    
    # 가져오는 여러방식 있음
    # 없는 페이지를 요청할때 만약 목록 5가 없는데 url에서 직접 /5로 치고 들어간다면 404로 보내줌
    todo = get_object_or_404(ToDo, id=id)

    return render(request, 'todo/todo_view.html', {'todo': todo})

def update(request, id):
    # todo = ToDo.objects.get(id=id)
    todo = get_object_or_404(ToDo, id=id)

    if request.method == 'POST':
        new_title = request.POST['new_title']
        new_description = request.POST['new_description']
        todo.title = new_title
        todo.description = new_description
        todo.save()
        return redirect('todo_view', todo.id) # todo.id 대신 id=id 써도 가능

    return render(request, 'todo/update.html', {'todo': todo})

def delete(request, id):
    # ToDo.objects.filter(id=id).delete()
    todo = get_object_or_404(ToDo, id=id)
    todo.delete()
    return redirect('todo')
