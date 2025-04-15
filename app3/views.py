from django.shortcuts import render
from django.http import HttpResponse

def sports(request):
    sports_data = 'this is sports page templates from views through context'
    return render(request, 'sports.html', {'data': sports_data,'sports_nav':True})

def tennis(request):
    tennis_data = 'this is cricket page templates from views through context'
    return render(request, 'cricket.html', {'data': tennis_data,'sports_nav':True})

def cricket(request):
    cricket_data = 'this is cricket page templates from views through context'
    return render(request, 'cricket.html', {'data': cricket_data,'sports_nav':True})

def football(request):
    football_data = 'this is football page templates from views through context'
    return render(request, 'football.html', {'data': football_data,'sports_nav':True})

def badminton(request):
    badminton_data = 'this is badminton page templates from views through context'
    return render(request, 'badminton.html', {'data': badminton_data,'sports_nav':True})
