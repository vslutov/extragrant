from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from .models import Question

# Create your views here.

def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/vote.html', {'question': question})

def recalc(request):
    if 'sure' in request.POST and request.POST['sure'] == "1":
        for question in Question.objects.all():
            votes = question.vote_set.count()
            question.average_score = float(sum(vote.choice.score for vote in question.vote_set.all())) / votes
            question.save()
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return render(request, 'polls/recalc.html')
