from project.apps import DLModelConfig
from pyproj import Transformer
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
from .json_copier import jsFileCopy
from .loadPL_Input import *
import numpy as np

import os


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
        result=0
        flag=0
        if flag==0:
            print("grid is executing")
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

        print("grid is finished")
        flag=1
        if flag==1:
        ## LOAD INPUTS FOR DEEP LEARNING MODEL (IMG_INPUT, NUMERICAL_INPUT)
        # img_input, numeric_input = load_input(str(214))

            if result != 0:
                details = Ap.objects.order_by("ap_idx")
                return render(request, "project/visualization.html", {"details": details})

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
    img_input, numeric_input = load_input(str(result.x_coord)+"_"+ str(result.y_coord))
    pathLossResult = DLModelConfig.DLModel.predict([img_input, numeric_input])
    pathLossResult-=120
    jsFileCopy(str(result.x_coord)+"_"+ str(result.y_coord), pathLossResult)
    transformer = Transformer.from_crs(32652, 4326)
    coords1 = transformer.transform(
        int(result.x_coord) - 200, int(result.y_coord) - 200
    )[0]
    coords2 = transformer.transform(
        int(result.x_coord) - 200, int(result.y_coord) - 200
    )[1]
    coords3 = transformer.transform(
        int(result.x_coord) + 200, int(result.y_coord) + 200
    )[0]
    coords4 = transformer.transform(
        int(result.x_coord) + 200, int(result.y_coord) + 200
    )[1]
    print(coords1)
    return render(
        request,
        "project/visualization_detail.html",
        {
            "result": result,
            "coords1": coords1,
            "coords2": coords2,
            "coords3": coords3,
            "coords4": coords4,
        },
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


# DLModel.summary()
