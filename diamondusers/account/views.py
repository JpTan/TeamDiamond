from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Student


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        array = ["", email]
        if user:
            login(request, user)
            count = Student.objects.filter(user=user).count()
            if count:
                student = Student.objects.get(user=user)
                return redirect('account:profile_url', pk=student.id_number)
            else:
                return redirect('account:login_url')
        else:
            array[0] = " Sorry! Email and Password didn't match, Please try again ! "
            return render(request, 'account/index.html', {'array': array})
    else:
        return render(request, 'account/index.html')


def user_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('First Name')
        last_name = request.POST.get('Last Name')
        id_number = request.POST.get('ID Number')
        college = request.POST.get('College')
        course = request.POST.get('Course')
        cellphone_number = request.POST.get('Cellphone Number')
        email = request.POST.get('Email')
        array = ["", first_name, last_name, id_number, college, course, cellphone_number, email]
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if not Student.objects.filter(id_number=id_number).exists():
            if pass_1 == pass_2:
                user = User.objects.create_user(username=email, email=email, password=pass_1)
                user.save()
                student = Student.objects.create(user=user, first_name=first_name, last_name=last_name, id_number=id_number, college=college, course=course, cellphone_number=cellphone_number)
                student.save()
                return redirect('account:login_url')
            else:
                array[0] = " Password Mismatch "
                return render(request, 'account/signup.html', {'array': array})
        else:
            array[0] = "Account " + id_number + " already exist"
            return render(request, 'account/signup.html', {'array': array})
    else:
        return render(request, 'account/signup.html')


def user_logout(request):
    logout(request)
    return redirect('account:login_url')


def user_profile(request, pk):
    student = Student.objects.get(pk=pk)
    array = ["", student.first_name, student.last_name, student.id_number, student.college, student.course, student.cellphone_number]
    if request.method == 'POST':
        first_name = request.POST.get('First Name')
        last_name = request.POST.get('Last Name')
        id_number = request.POST.get('ID Number')
        college = request.POST.get('College')
        course = request.POST.get('Course')
        cellphone_number = request.POST.get('Cellphone Number')
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if pass_1 == pass_2:
            user = student.user
            student.first_name = first_name
            student.last_name = last_name
            student.id_number = id_number
            student.college = college
            student.course = course
            student.cellphone_number = cellphone_number
            user.set_password(pass_1)
            user.save()
            student.save()
            return redirect('account:profile_url', pk=student.id_number)
        else:
            array[0] = " Password Mismatch "
            return render(request, 'account/profile.html', {'array': array})
    else:
        return render(request, 'account/profile.html', {'array': array})
