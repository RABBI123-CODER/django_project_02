from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def rabbi_002(request):
    return HttpResponse('<h1>this is rabbi_002 app and it is my project.. <br />using by second app </h1>')
