from django.shortcuts import render, redirect
from dbhandler.models import Student, Loan, Payment


def index(request):
    return render(request, 'index.html')


def view_applicants(request):
    applicant_list = Student.objects.filter(loan__status="In Process")
    return render(request, 'applicants.html', {'applicant_list': applicant_list})
    # to pass variables into the template, define a context (with file type dict)
    # the first parameter is the name, second is the value/variable


def view_applicant_detail(request, idnum):
    student = Student.objects.get(idNum=idnum)
    return render(request, 'details.html', {'student': student})


def delete_student(request, idnum):
    Student.objects.get(pk=idnum).delete()
    view_applicants(request)
