from django.db import models

# Create your models here.


class Question(models.Model):

    question_text = models.CharField(max_length=128)
    published_at = models.DateTimeField('published at')


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
