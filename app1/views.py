from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    home_data='this is home page templates from views through context '
    #home_data2=['item1','item2','item3']
    home_data2={'key1':'poojitha'}
    li=[
        {'title':'india',
         'desc':'this is all about india'},
         {'title': 'artificial intel',
          'desc':'this is all artificial intel'}
    ]
    return render(request, 'home.html', {'data': home_data, 'data2': home_data2}) 

def about(request):
    about_data='this is about page templates from views through context '
    return render(request,'about.html',{'data':about_data})



