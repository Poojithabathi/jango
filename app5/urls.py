from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movies),
    path('tollywood/', views.tollywood),
    path('bollywood/', views.bollywood),
    path('hollywood/', views.hollywood),
    path('kollywood/', views.kollywood),
]