from django.shortcuts import render
from django.http import HttpResponse

def electronics(request):
    electronics_data = 'This is the electronic page template from views through context'
    return render(request, 'electronics.html', {'data': electronics_data,'electronics_nav':True})

def mobile(request):
    mobile_data = 'This is the mobile page template from views through context'
    return render(request, 'mobile.html', {'data': mobile_data,'electronics_nav':True})

def web(request):
    web_data = 'This is the web page template from views through context'
    return render(request, 'web.html', {'data': web_data,'electronics_nav':True})

def laptop(request):
    laptop_data = 'This is the laptop page template from views through context'
    return render(request, 'laptop.html', {'data': laptop_data,'electronics_nav':True})

def watch(request):
    watch_data = 'This is the watch page template from views through context'
    return render(request, 'watch.html', {'data': watch_data,'electronics_nav':True})

