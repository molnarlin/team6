from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def team_view(request):
    return render(request, 'team.html')