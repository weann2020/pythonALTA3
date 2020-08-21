# Create your models here.

import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # You can use an optional first positional argument to a Field to designate a human-readable name.
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # ForeignKey tells Django each Choice
    # is related to a single Question
    # Django supports common database relationships:
    # many-to-one, many-to-many, and one-to-one

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
         return self.choice_text
