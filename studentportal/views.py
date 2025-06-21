from django.shortcuts import render, HttpResponse

from . import models

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)


def signup(request):
    context = {}
    return render(request, 'signup.html', context)