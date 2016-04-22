from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_text = models.DateField("date published")

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Answer(models.Model):
    def __str__(self):
        return self.ans_text
    question = models.ForeignKey(Question)
    ans_text = models.CharField(max_length=200)

