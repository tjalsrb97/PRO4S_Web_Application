from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('introduction/', views.introduction, name='introduction'),
    path('research_result/', views.research_result, name='research_result'),
    path('path_loss_predict/', views.path_loss_predict, name='path_loss_predict'),
    path('dashboard/', views.dashboard, name='dashboard'),
]