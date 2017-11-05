from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("<h1> HomePage or Index View </h1>")


@login_required()
def home(request):
    return render(request, 'student/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'student/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'student/signup.html', {'form': form})


def logout(request):
    return render(request, 'student/home.html')


def login(request):
    return render(request, 'student/login.html')


