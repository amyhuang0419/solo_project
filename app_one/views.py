from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to my solo project!!")
