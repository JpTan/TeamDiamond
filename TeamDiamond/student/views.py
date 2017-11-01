from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


# Create your views here.
def index(request):
    return HttpResponse("<h1> HomePage or Index View </h1>")
    # template = loader.get_template('student')
    # context = {
    #     # stuff needed
    # }
    # return HttpResponse(template.render(context, request))


def UserFormView(request):
    return HttpResponse("<h1> Registration View </h1>")
    # form_class = UserForm
    # template_name = 'student/registration_form.html'
    #
    # # display blank form
    # def get(self, request):
    #     form = self.form_class(None)
    #     return render(request, self.template_name, {'form': form})
    #
    # # process form data
    # def post(self, request):
    #     form = self.form_class(request.POST)
    #
    #     if form.is_valid():
    #         # store locally
    #         user = form.save(commit=False)
    #
    #         # cleaned (normalized) data
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         user.set_password(password)
    #         user.save()
    #
    #         # return User objects if credentials are correct
    #         user = authenticate(email=email, password=password)
    #
    #         if user is not None:
    #
    #             if user.is_active:
    #                 login(request, user)
    #                 return redirect('student:index')
    #
    #     # return blank form if something went wrong
    #     return render(request, self.template_name, {'form': form})