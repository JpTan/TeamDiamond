from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import UserForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'student/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
         "form": form,
    }
    return render(request, 'student/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login_user(request, user)
                return render(request, 'student/base.html')
            else:
                return render(request, 'student/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'student/login.html', {'error_message': 'Invalid login'})
    return render(request, 'student/login.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UserForm()
    return render(request, 'student/register.html', {'form': form})


def homepage(request):
    return render(request, 'student/homepage.html')