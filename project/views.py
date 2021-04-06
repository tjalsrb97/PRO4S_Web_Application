from django.shortcuts import render
from django.utils import timezone

def introduction(request):
    return render(request, 'project/intro.html', {})

def research_result(request):
    return render(request, 'project/result.html', {})

def path_loss_predict(request):
    return render(request, 'project/predict.html', {})

def dashboard(request):
    return render(request, 'project/board.html', {})

def login(request):
    return render(request, 'project/login.html', {})

