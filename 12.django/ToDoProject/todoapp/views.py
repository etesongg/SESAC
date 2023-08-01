from django.shortcuts import render, redirect
from .models import ToDo

# Create your views here.

def home(request):
    return render(request, 'index.html')

def todo(request):
    # db로 부터 메세지 받아오기 (orm을 사용해서)
    todos = ToDo.objects.all()
    return render(request, 'todo.html', {'todos' : todos})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        ToDo.objects.create(title=title, description=description)
        return redirect('todo')

    return render(request, 'create.html')

def todo_view(request, id):
    todo = ToDo.objects.get(id=id)
    return render(request, 'todo_view.html', {'todo': todo})

def update(request, id):
    todo = ToDo.objects.get(id=id)
    if request.method == 'POST':
        new_title = request.POST['new_title']
        new_description = request.POST['new_description']
        todo.title = new_title
        todo.description = new_description
        todo.updated_at = todo.updated_at
        todo.save()
        return redirect('todo')

    return render(request, 'update.html', {'todo': todo})

def delete(request, id):
    ToDo.objects.filter(id=id).delete()
    return redirect('todo')
