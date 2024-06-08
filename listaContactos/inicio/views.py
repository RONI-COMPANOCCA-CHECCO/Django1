from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myHomeView(*args, **kwargs):
    return HttpResponse("<h1>HOLA MUNDO DESDE DJANGO</h1>")
