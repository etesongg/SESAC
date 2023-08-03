from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

# Create your views here.
def polls(request):
    questions = Question.objects.all()
    return render(request, 'polls/polls_list.html', {'questions': questions})

def poll_detail(request, ques_id):
    # poll_choice = get_object_or_404(Choice, id=ques_id)
    poll_choice = Question.objects.get(id=ques_id)
    poll_choice = poll_choice.choice_set.all()
    print(poll_choice)
    return render(request, 'polls/poll_detail.html', {'poll_choice': poll_choice})




