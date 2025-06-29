from django.shortcuts import render, HttpResponse

from . import models

# Create your views here.
def home(request):
    students = models.Student.objects.all()
    student = students[0]
    student.full_name = f"{student.first_name} {student.last_name}"
    context = {"student": student}
    return render(request, 'home.html', context)


def signup(request):
    context = {}
    return render(request, 'signup.html', context)