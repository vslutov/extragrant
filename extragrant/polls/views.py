from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from .models import Question, Choice, Count

# Create your views here.

def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    count_chart = []
    for count in question.count_set.order_by('choice__score').all():
        count_chart.append([count.choice.score, count.count])
    return render(request, 'polls/result.html', {'question': question, 'count_chart': count_chart})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/vote.html', {'question': question})

def recalc(request):
    if 'sure' in request.POST and request.POST['sure'] == "1":
        for question in Question.objects.all():
            for choice in Choice.objects.all():
                count, created = Count.objects.get_or_create(question=question, choice=choice)
                count.count = question.vote_set.filter(choice=choice).count()
                count.save()

            votes = question.vote_set.count()
            question.average_score = float(sum(count.count * count.choice.score for count in question.count_set.all())) / votes
            question.save()
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return render(request, 'polls/recalc.html')
