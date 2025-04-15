from django.urls import path
from . import views

urlpatterns = [
    path('sports/',views.sports),
    path('tennis/', views.tennis),
    path('cricket/', views.cricket),
    path('football/', views.football),
    path('badminton/', views.badminton),
]