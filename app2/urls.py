from django.urls import path
from . import views

urlpatterns = [
    path('electronics/', views.electronics),
    path('mobile/', views.mobile),
    path('web/', views.web),
    path('laptop/', views.laptop),
    path('watch/', views.watch),
]