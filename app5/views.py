from django.shortcuts import render
from django.http import HttpResponse

def movies(request):
    movies_data = 'this is movies page templates from views through context'
    return render(request, 'movies.html', {'data': movies_data})

def tollywood(request):
    tollywood_data = 'this is tollywood page templates from views through context'
    return render(request, 'tollywood.html', {'data': tollywood_data})

def bollywood(request):
    bollywood_data = 'this is bollywood page templates from views through context'
    return render(request, 'bollywood.html', {'data': bollywood_data})

def hollywood(request):
    hollywood_data = 'this is hollywood page templates from views through context'
    return render(request, 'hollywood.html', {'data': hollywood_data})

def kollywood(request):
    kollywood_data = 'this is kollywood page templates from views through context'
    return render(request, 'kollywood.html', {'data': kollywood_data})
