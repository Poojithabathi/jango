from django.shortcuts import render
from django.http import HttpResponse


def fashion(request):
    fashion_data = 'this is fashion page templates from views through context'
    return render(request, 'fashion.html', {'data': fashion_data})

def shirt(request):
    shirt_data = 'this is shirt page templates from views through context'
    return render(request, 'shirt.html', {'data': shirt_data})

def pant(request):
    pant_data = 'this is pant page templates from views through context'
    return render(request, 'pant.html', {'data': pant_data})

def shoes(request):
    shoes_data = 'this is shoes page templates from views through context'
    return render(request, 'shoes.html', {'data': shoes_data})

def kurtis(request):
    kurtis_data = 'this is kurtis page templates from views through context'
    return render(request, 'kurtis.html', {'data': kurtis_data})
