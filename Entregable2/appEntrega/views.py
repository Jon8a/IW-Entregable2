from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 return HttpResponse("Hello, world!")

"""Pantalla principal"""
def principal(request):
    return render(request, 'principal.html')