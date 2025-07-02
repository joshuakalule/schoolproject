from pprint import pprint
from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from .forms import SignUpForm, LoginForm
from .utils import compile_score_table

# Create your views here.


def redirect_to_login(request):
    return redirect('user_login')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        student = models.Student.objects.filter(username=username).first()
        if student:
            if student.password == password:
                return redirect('home', username=username)

        form = LoginForm(initial={'username': username})
        errors = ["Invalid username or password"]
        return render(request, "login.html",  {"form": form, "errors": errors})
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "login.html",  context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # process the data here
            student = form.save(commit=False)
            username = student.username
            if models.Student.objects.filter(username=username):
                errors = ["A user with those names already exists"]
                form = SignUpForm(initial={'class_name': 'S1'})
                return render(request, "signup.html", {"form": form, "errors": errors})

            form.save()
            return redirect('home', username=username)
    else:
        form = SignUpForm(initial={'class_name': 'S1'})
    context = {
        "form": form
    }
    return render(request, "signup.html", context)


def home(request, username):
    student = models.Student.objects.filter(username=username).first()
    if not student:
        return redirect('user_login')
    pprint(student.compile_scores())
    pprint(compile_score_table(student.compile_scores()))
    scores_header, scores_data = compile_score_table(student.compile_scores())
    context = {
        "student": student,
        "scores_header": scores_header,
        "scores_data": scores_data
    }
    return render(request, 'home.html', context)
