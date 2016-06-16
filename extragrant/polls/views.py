from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.translation import ugettext as _

from .models import Question

def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions, 'title': _("Question list")})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question, 'title': _("Question result")})

def vote(request, question_id):
    return HttpResponse("You 're voting a question {id}".format(id=question_id))

# Create your views here.
