from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="reindex"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("index/", views.index, name="index"),
    path("introduction/", views.introduction, name="introduction"),
    path("analysis/", views.analysis, name="analysis"),
    path("site_configuration/", views.site_configuration, name="site_configuration"),
    path("visualization/", views.visualization, name="visualization"),
]
