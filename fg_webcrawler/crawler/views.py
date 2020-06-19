from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Welcome to webcrawler')

def documentation(request):
    pass

def downloads(request):
    pass