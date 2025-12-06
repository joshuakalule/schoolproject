from pprint import pprint
from django.shortcuts import render, redirect
from . import models
from .utils import compile_score_table


def home(request, username):
    student = models.Student.objects.filter(username=username).first()
    if not student:
        return redirect('portal-login')
    pprint(student.compile_scores())
    pprint(compile_score_table(student.compile_scores()))
    scores_header, scores_data = compile_score_table(student.compile_scores())
    context = {
        "student": student,
        "scores_header": scores_header,
        "scores_data": scores_data
    }
    return render(request, 'home.html', context)
