from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from .models import Student
from django.views import generic


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            student = Student.objects.get(user=user)
            return HttpResponseRedirect('/account/home/')
            #return redirect('account.views.home_view.as_view()', pk=student.pk)
        else:
            error = " Sorry! Email and Password didn't match, Please try again ! "
            return render(request, 'account/index.html', {'error': error})
    else:
        return render(request, 'account/index.html')


def user_signup(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        first_name = request.POST.get('First Name')
        last_name = request.POST.get('Last Name')
        id_number = request.POST.get('ID Number')
        college = request.POST.get('College')
        course = request.POST.get('Course')
        cellphone_number = request.POST.get('Cellphone Number')
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if pass_1 == pass_2:
            user = User.objects.create_user(username=email, email=email, password=pass_1)
            user.save()
            student = Student.objects.create(user=user, first_name=first_name, last_name=last_name, id_number=id_number, college=college, course=course, cellphone_number=cellphone_number)
            student.save()
            return HttpResponseRedirect('/account/login/')
        else:
            error = " Password Mismatch "
            return render(request, 'account/signup.html', {'error': error})
    else:
        return render(request, 'account/signup.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')


class home_view(generic.DetailView):
    model = Student
    template_name = 'account/home.html'
