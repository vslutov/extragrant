# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Criterion(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.code + ' - ' + self.description

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    average_score = models.FloatField(default=0)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    SCORE_CHOICES = (
         (ZERO, '0'),
         (ONE, '1'),
         (TWO, '2'),
         (THREE, '3'),
         (FOUR, '4'),
         (FIVE, '5'),
    )

    score_choice = models.IntegerField(choices=SCORE_CHOICES, default=ZERO)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.score_choice)
