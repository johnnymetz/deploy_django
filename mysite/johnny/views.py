from django.shortcuts import render


def index(request):
    athlete_list = [
        {'name': 'Steve Nash', 'ppg': 19.7, 'active': False},
        {'name': 'LBJ', 'ppg': 27.2, 'active': False},
        {'name': 'Russell Westbrook', 'ppg': 24.5, 'active': False},
        {'name': 'James Harden', 'ppg': 26.8, 'active': False},
    ]
    context = {
        'athlete_list': athlete_list
    }
    return render(request, 'johnny/index.html', context)
