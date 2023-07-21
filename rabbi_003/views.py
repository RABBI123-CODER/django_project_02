from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def rabbi_003(request):
    return HttpResponse('<h1>this is rabbi_003 app and it is my project..<br /> and it is my third app..</h1>')
