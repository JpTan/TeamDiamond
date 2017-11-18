from django.shortcuts import render, redirect, render_to_response
from dbhandler.models import Student, Loan, Payment
from django.views.generic import View
from .forms import PaymentForm
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def view_applicants(request):
    applicant_list = Student.objects.filter(loan__status="In Process")

    return render(request, 'applicants.html', {'applicant_list': applicant_list})
    # to pass variables into the template, define a context (with file type dict)
    # the first parameter is the name, second is the value/variable


# class ApplicantView(generic.ListView):
#     template_name = 'applicants.html'
#     context_object_name = 'applicant_list'
#
#     def get_queryset(self):
#         return Student.objects.filter(loan__status="In Process")


# class ApplicantDetail(generic.DetailView):
#     model = Student
#     template_name = 'app_details.html'


def view_applicant_detail(request, idnum):
    student = Student.objects.get(idNum=idnum)
    loan = Loan.objects.get(idNum=student)
    return render(request, 'app_details.html', {'student': student, 'loan': loan})


def delete_student(request, idnum):
    Student.objects.get(pk=idnum).delete()
    return redirect('oas:view_applicants')


def approve_loan(request, idnum):
    student = Student.objects.get(idNum=idnum)
    loan = Loan.objects.get(idNum=student)
    loan.status = "Approved"
    loan.balance = loan.amount
    loan.save()
    return render(request, 'app_details.html', {'student': student, 'loan': loan})


def reject_loan(request, idnum):
    student = Student.objects.get(idNum=idnum)
    loan = Loan.objects.get(idNum=student)
    loan.status = "Rejected"
    loan.save()
    return render(request, 'app_details.html', {'student': student, 'loan': loan})


def view_loaners(request):
    loaners = Student.objects.filter(loan__status="Approved")
    return render(request, 'loaners.html', {'loaners': loaners})


def view_loaner_detail(request, idnum):
    student = Student.objects.get(idNum=idnum)
    loan = Loan.objects.get(idNum=student)
    return render(request, 'loaner_details.html', {'student': student, 'loan': loan})


def view_payments_pending(request):
    payments = Payment.objects.filter(isApproved=False)
    show_all = False
    return render(request, 'payments.html', {'payments': payments, 'show_all': show_all})


def view_payments_all(request):
    payments = Payment.objects.all()
    show_all = True
    return render(request, 'payments.html', {'payments': payments, 'show_all': show_all})


def view_payment_detail(request, pk):
    payment = Payment.objects.get(pk=pk)
    student = Student.objects.get(idNum=payment.idNum.idNum)
    loan = Loan.objects.get(idNum=student)
    return render(request, 'payment_details.html', {'student': student, 'payment': payment, 'loan': loan})


def approve_payment(request, pk):
    payment = Payment.objects.get(pk=pk)
    payment.isApproved = True
    payment.save()
    student = Student.objects.get(idNum=payment.idNum.idNum)
    loan = Loan.objects.get(idNum=student)
    loan.balance -= payment.amount
    loan.save()
    return redirect('oas:view_payment_detail', pk=pk)


def reject_payment(request, pk):
    Payment.objects.get(pk=pk).delete()
    return redirect('oas:all_payments')


# def edit_payment(request, ornum):
#     payment = Payment.objects.get(orNum=ornum)
#     student = Student.objects.get(idNum=payment.idNum.idNum)
#     loan = Loan.objects.get(idNum=student)
#     return render(request, 'payment_edit.html', {'student': student, 'payment': payment, 'loan': loan})


def edit_payment(request, pk):
    payment = Payment.objects.get(pk=pk)
    student = Student.objects.get(idNum=payment.idNum.idNum)
    loan = Loan.objects.get(idNum=student)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            paymentf = form.save(commit=False)
            paymentf.idNum = student
            paymentf.isApproved = False
            payment.delete()
            paymentf.save()
            # payment.orNum = paymentF.orNum
            # payment.amount = paymentF.amount
            # payment.date = paymentF.date
            # payment.save()

            return redirect('oas:view_payment_detail', pk=paymentf.pk)
    else:
        form = PaymentForm(None, initial={'orNum': payment.orNum, 'amount': payment.amount, 'date': payment.date})

    return render(request, 'payment_edit.html', {'form': form, 'student': student, 'payment': payment, 'loan': loan})

#
# class PaymentView(View):
#     form_class = PaymentForm
#     template_name = 'payment_edit.html'
#
#     # display blank form
#     def get(self, request, ornum):
#         payment = Payment.objects.get(orNum=ornum)
#         student = Student.objects.get(idNum=payment.idNum.idNum)
#         loan = Loan.objects.get(idNum=student)
#         form = self.form_class(None, initial={'orNum': payment.orNum, 'amount': payment.amount, 'date': payment.date})
#
#             if form.is_valid():
#                 payment = form.save(commit=False)
#                 payment.save()
#                 return redirect('oas:view_payment_detail', ornum=ornum)
#
#         return render(request, self.template_name, {'form': form, 'student': student, 'payment': payment, 'loan': loan})
#
#     # process form data
#     def post(self, request, ornum):
#         payment = Payment.objects.get(orNum=ornum)
#         student = Student.objects.get(idNum=payment.idNum.idNum)
#         loan = Loan.objects.get(idNum=student)
#         form = self.form_class(request.POST, initial={'orNum': payment.orNum, 'amount': payment.amount, 'date': payment.date})
#
#         if form.is_valid():
#             payment = form.save(commit=False)
#             payment.save()
#             return redirect('oas:view_payment_detail', ornum=ornum)
#
#         return render(request, self.template_name, {'form': form, 'student': student, 'payment': payment, 'loan': loan})
