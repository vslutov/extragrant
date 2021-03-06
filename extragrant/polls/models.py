# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class Criterion(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=500)

    def __str__(self):
        return (_("{code} : {description}")
                .format(code=self.code, description=self.description))

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    average_score = models.FloatField(default=0)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

@python_2_unicode_compatible
class Choice(models.Model):
    score = models.FloatField(default=0)

    def __str__(self):
        return str(self.score)

@python_2_unicode_compatible
class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (_("{user} voted at {choice} by {question}")
                .format(user=self.user, question=self.question,
                    choice=self.choice))

@python_2_unicode_compatible
class Count(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return (_("{count} users voted at {choice} by {question}")
                .format(count=self.count, question=self.question,
                        choice=self.choice))

@python_2_unicode_compatible
class Voting(models.Model):
    user = models.ForeignKey(User, unique=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (_('{user} voted at {time}')
                .format(user=self.user, time=self.last_modified))
