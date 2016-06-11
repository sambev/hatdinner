import random
import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse

from dinner.models import Vote


@csrf_exempt
def index(request):
    if request.method == 'GET':
        votes = Vote.objects.all()
        print(votes)
        return render(request, 'index.html', {
            'votes': votes
        })

    if request.method == 'POST':
        vote = Vote(name=request.POST['name'], dinner=request.POST['dinner'])

        if len(vote.name) and len(vote.dinner):
            vote.save()

        return redirect('/')

    if request.method == 'PUT':
        votes = Vote.objects.all()
        winner = votes[random.randint(0, len(votes) - 1)]

        return HttpResponse(json.dumps({
            'name': winner.name,
            'dinner': winner.dinner,
        }), 200)

    if request.method == 'DELETE':
        Vote.objects.all().delete()
        return HttpResponse(None, 200)
