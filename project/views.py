from django.shortcuts import render
from django.utils import timezone
from .forms import APForm
from django.shortcuts import redirect


def introduction(request):
    return render(request, 'project/intro.html', {})

def research_result(request):
    return render(request, 'project/result.html', {})

def path_loss_predict(request):
    if request.method == "POST":
        form = APForm(request.POST)
        print(form)
        if form.is_valid():
            ap = form.save(commit=False)
            ap.author = request.user
            ap.save()
    else:
        form = APForm()
    return render(request, 'project/predict.html', {'form': form})

def dashboard(request):
    return render(request, 'project/board.html', {})

def login(request):
    return render(request, 'project/login.html', {})

