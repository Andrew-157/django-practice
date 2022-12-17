from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):

    question_list = Question.objects.order_by('-published_at')[:10]

    response = '/n'.join([q.question_text for q in question_list])

    return HttpResponse(response)


def poll(request, poll_id):

    return HttpResponse(f'Poll {poll_id}')
