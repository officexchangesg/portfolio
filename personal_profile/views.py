from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hi Welcome")
# Create your views here.