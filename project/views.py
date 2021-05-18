from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import UserExperiment, Result, Ap
from .forms import APForm
import os

# loading time
# from .lams_on_svr import exit


@login_required
def introduction(request):
    return render(request, "project/intro.html", {})


@login_required
def analysis(request):
    return render(request, "project/analysis.html", {})


@login_required
def site_configuration(request):
    if request.method == "POST":
        form = APForm(request.POST)
        if form.is_valid():
            ap = form.save(commit=False)
            ap.time = timezone.now()
            ap.save()
            result = os.popen(
                "python project/grid.py"
                + " "
                + str(ap.x_coord)
                + "_"
                + str(ap.y_coord)
                + " "
                + str(ap.x_coord)
                + " "
                + str(ap.y_coord)
                + " "
                + str(ap.azimuth)
                + " "
                + str(ap.downtilt)
            ).read()
            if result != 0:
                return render(
                    request,
                    "project/visualization_detail.html",
                    {"ap": ap},
                )

    else:
        form = APForm()

    return render(request, "project/configurate.html", {"form": form})


@login_required
def visualization(request):
    details = Ap.objects.order_by("ap_idx")
    return render(request, "project/visualization.html", {"details": details})


@login_required
def visualization_detail(request, pk):
    result = get_object_or_404(Ap, pk=pk)
    return render(
        request,
        "project/visualization_detail.html",
        {"result": result},
    )


def index(request):
    return render(request, "project/index.html")


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return render(
            request,
            "project/intro.html",
            {"user": user},
        )
    else:
        messages.error(request, "invalid login")
        return redirect("index")


def logout(request):
    auth_logout(request)
    return redirect("index")


def not_authenticated(request):
    if not request.user.is_authenticated:
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))


# from tensorflow.keras.models import load_model

# DLModel = load_model("./project/static/DLModel/20_20_100_v1_0510_jh1.h5")
# DLModel.summary()
