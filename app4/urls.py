from django.urls import path
from . import views

urlpatterns = [
    path('fashion/', views.fashion),
    path('shirt/', views.shirt),
    path('pant/', views.pant),
    path('shoes/', views.shoes),
    path('kurtis/', views.kurtis),
]