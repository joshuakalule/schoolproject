from django.shortcuts import render, redirect
from studentportal import forms as studentportal_forms, models as studentportal_models
from teacherportal import forms as teacherportal_forms, models as teacherportal_models
import json

ASSET_MAP = {
    'student': {
        'signup_form': studentportal_forms.SignUpForm,
        'login_form': studentportal_forms.LoginForm,
        'models': studentportal_models,
        'signup_template': 'studentportal/signup.html',
        'home_template': 'studentportal/home.html'
    },
    'teacher': {
        'signup_form': teacherportal_forms.SignUpForm,
        'login_form': teacherportal_forms.LoginForm,
        'models': teacherportal_models,
        'signup_template': 'teacherportal/signup.html',
        'home_template': 'teacherportal/home.html'
    },
    'parent': {
        'signup_form': '',
        'login_form': '',
        'models': '',
        'signup_template': '',
        'home_template': ''
    },
    'administrator': {
        'signup_form': '',
        'login_form': '',
        'models': '',
        'signup_template': '',
        'home_template': ''
    }
}

def redirect_to_login(request):
    return redirect('portal-login', 'student')

def redirect_to_signup(request):
    return redirect('portal-signup', 'student')

def login(request, user_type):
    form = studentportal_forms.LoginForm()
    role = request.POST.get('user', None)
    if role:
        print("Role selected: ", role)
        return redirect('portal-login', user_type=role)
    user_assets = ASSET_MAP.get(user_type)
    login_form = user_assets.get('login_form', None)
    models = user_assets.get('models', None)
    if models is None:
        return f"Server Error: user_type '{user_type}' returned models 'None'"
    if login_form is None:
        return redirect('portal-login')
    if request.method == 'POST':
        form = login_form(request.POST)
        if models is None:
            errors = [f"unknown model selection of (role)[{user_type}] "]
            return render(request, "login.html", {"form": form, "errors": errors})

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

        student = models.Student.objects.filter(username=username).first()

        if student:
            if student.password == password:
                return redirect('home', username=username)

        form = login_form(initial={'username': username})
        errors = ["Invalid credentials"]
        return render(request, "login.html",  {"form": form, "errors": errors})
    else:
        form = login_form()
    context = {
        "form": form,
        "user_type": user_type
    }
    return render(request, "login.html",  context)

def signup(request, user_type):
    role = request.POST.get('user', None)
    if role:
        print("Role selected: ", role)
        return redirect('portal-signup', user_type=role)

    user_assets = ASSET_MAP.get(user_type)
    signup_form = user_assets.get('signup_form', None)
    models = user_assets.get('models', None)
    signup_template = user_assets.get('signup_template', 'signup.html')
    if models is None:
        return f"Server Error: user_type '{user_type}' returned models 'None'"
    if signup_form is None:
        return redirect('portal-signup')
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            # process the data here
            user = form.save(commit=False)
            username = user.username

            user = form.save()
            username = user.username
            return redirect('home', username=username)
        form = signup_form()
        errors = ["Invalid credentials"]
        return render(request, signup_template, {"form": form, "errors": errors})
    else:
        form = signup_form()
    context = {
        "form": form,
        "user_type": user_type
    }
    return render(request, signup_template, context)