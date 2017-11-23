from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Student
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string


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
            array[0] = " Sorry! Email and Password didn't match or Account is not yet Verified, Please try again ! "
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
        if (not Student.objects.filter(id_number=id_number).exists()) and (not User.objects.filter(username=email).exists()):
            if pass_1 == pass_2:
                user = User.objects.create_user(username=email, email=email, password=pass_1)
                user.is_active = False
                user.save()
                student = Student.objects.create(user=user, first_name=first_name, last_name=last_name, id_number=id_number, college=college, course=course, cellphone_number=cellphone_number)
                student.save()
                current_site = get_current_site(request)
                message = render_to_string('account/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                mail_subject = 'Activate your account.'
                to_email = user.email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
            else:
                array[0] = " Password Mismatch "
                return render(request, 'account/signup.html', {'array': array})
        else:
            array[0] = "Account already exist"
            return render(request, 'account/signup.html', {'array': array})
    else:
        return render(request, 'account/signup.html')


def user_logout(request):
    logout(request)
    return redirect('account:login_url')


def user_profile(request, pk):
    student = Student.objects.get(pk=pk)
    array = ["", student.first_name, student.last_name, student.id_number, student.college, student.course, student.cellphone_number, student.user.email]
    if request.method == 'POST':
        first_name = request.POST.get('First Name')
        last_name = request.POST.get('Last Name')
        college = request.POST.get('College')
        course = request.POST.get('Course')
        cellphone_number = request.POST.get('Cellphone Number')
        current_password = request.POST.get('current_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        user = authenticate(username=student.user.username, password=current_password)
        if user:
            user = student.user
            student.first_name = first_name
            student.last_name = last_name
            student.college = college
            student.course = course
            student.cellphone_number = cellphone_number
            if new_password1 != "" and new_password1 == new_password2:
                user.set_password(new_password1)
            elif new_password1 != new_password2:
                array[0] = " Password Mismatch "
                return render(request, 'account/profile.html', {'array': array})
            user.save()
            student.save()
            return redirect('account:profile_url', pk=student.id_number)
        else:
            array[0] = " Wrong Password "
            return render(request, 'account/profile.html', {'array': array})
    else:
        return render(request, 'account/profile.html', {'array': array})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:login_url')
    else:
        return HttpResponse('Activation link is invalid!')
