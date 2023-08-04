from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice

# Create your views here.
def polls(request):
    questions = Question.objects.all()
    return render(request, 'polls/polls_list.html', {'questions': questions})

def poll_detail(request, ques_id):
    # poll_choice = get_object_or_404(Choice, id=ques_id)
    poll_choice = Choice.objects.filter(question=ques_id).all()
    if request.method == 'POST':
        select_choice = request.POST['choice']
        choice = Choice.objects.get(id=select_choice)
        choice.votes += 1
        choice.save()
        return redirect('poll_result', ques_id, choice.id)
    return render(request, 'polls/poll_detail.html', {'poll_choice': poll_choice})

def poll_result(request, ques_id, chois_id):
    results = Choice.objects.filter(question=ques_id).all()
    title = Question.objects.get(id=ques_id)
    if request.method == 'POST':
        choice = Choice.objects.get(id=chois_id)
        choice.votes -= 1
        choice.save()
        return redirect('poll_detail', ques_id )
    return render(request, 'polls/poll_result.html', {'results': results, 'title': title})




