from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def captain(request):
    return HttpResponse('<h1>Hardik Pandiya</h1>')

def vicecap(request):
    return HttpResponse('<h1>SKY</h1>')
