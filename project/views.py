from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import UserExperiment, Result, Ap
from .forms import APForm




@login_required
def introduction(request):
    return render(request, "project/intro.html", {})


@login_required
def research_result(request):
    return render(request, "project/result.html", {})


@login_required
def path_loss_predict(request):
    if request.method == "POST":
        form = APForm(request.POST)
        if form.is_valid():
            ap = form.save(commit=False)
            ap.author = request.user
            ap.save()
    else:
        form = APForm()
    return render(request, 'project/predict.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, "project/board.html", {})


def index(request):
    return render(request, "project/index.html")


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return render(request, "project/intro.html", {"user": user},)
    else:
        messages.error(request, "invalid login")
        return redirect("index")


def logout(request):
    auth_logout(request)
    return redirect("index")


def not_authenticated(request):
    if not request.user.is_authenticated:
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))


# def handler404(request, exception):
#     context = {}
#     response = render(request, "project/404.html", context=context)
#     response.status_code = 404
#     return response


# def custom500(request):
#     return render(request, "project/500.html", {})


# @csrf_exempt
# def signup(request):
#     template_name = 'login.html'
#     data = request.POST
#     if User.objects.filter(user_id= data['id']).exists():
#         context = {
#             "result" : "이미 존재하는 아이디입니다."
#         }
#         return HttpResponse(json.dumps(context),content_type="application/json")
#     else :
#         User.objects.create(
#             user_id = data['id'] ,
#             email = data['email'] ,
#             password = data['password'],
#         ).save()
#         context = {
#             "result" : "회원가입 성공"
#         }
#         return HttpResponse(json.dumps(context),content_type="application/json")

# @csrf_exempt
# def loginCheck(request):
#     template_name = 'login.html'
#     request.session['loginOk'] = False
#     try:
#         data = request.POST
#         inputId = data['id']
#         inputPassword = data['password']

#     except (KeyError,inputId == "",inputPassword == "") :
#         context = {
#             "uid" : "empty",
#             "upass" : "empty",
#         }
#         return render(request,template_name,context)
#     else :
#         if User.objects.filter(user_id= inputId).exists():
#             getUser = User.objects.get(user_id = inputId)
#             if getUser.password == inputPassword :
#                 request.session['loginOk'] = True
#                 context = {
#                     "result" : "로그인 성공"
#                 }
#             else :
#                 request.session['loginOk'] = False
#                 context = {
#                     "result" : "비밀번호가 틀렸습니다"
#                 }
#         else :
#             request.session['loginOk'] = False
#             context = {
#                 "result" : "존재하지 않는 id입니다"
#             }
#         return HttpResponse(json.dumps(context),content_type="application/json")
