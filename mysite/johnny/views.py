from django.shortcuts import render
from .models import Athlete


def index(request):
    context = {
        'athlete_list': Athlete.objects.all()
    }
    return render(request, 'johnny/index.html', context)
