from .models import Payment, Loan
from django.views import generic
from django.views.generic import CreateView
from django.shortcuts import HttpResponse, render


# Create your views here.
# sample homepage
class IndexView(generic.ListView):
    template_name = 'sample/index.html'
    context_object_name = 'loan_details'

    def get_queryset(self):
        return Loan.objects.filter()  # check id number


# view payments already made by the student
class PaymentLView(generic.ListView):
    template_name = 'sample/view_payments.html'

    def get_queryset(self):
        return Payment.objects.filter()  # check id number


class PaymentDView(generic.DetailView):
    model = Payment
    template_name = 'sample/view_payment_details.html'


class PaymentCreate(CreateView):
    model = Payment
    fields = ['orNum', 'amount', 'date', 'idNum', 'isApproved']


# view status of application
def view_status(request):
    return HttpResponse("<h1> Lorem Ipsum </h1>")


# loan calculator
def loan_calc(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount_field', None))
        start_month = int(request.POST.get('smonth_field', None))
        end_month = int(request.POST.get('emonth_field', None))
        result = amount
        length = end_month-start_month

        # Calculate for interest at 3rd Month onwards
        if length > 2:
            for x in range(2, length):
                result += result * 0.01

        return HttpResponse("Result: " + str(result) + " Start: " + str(start_month) + " End: " + str(end_month))

    else:
        return render(request, 'sample/calculator_form.html')


# loan projection view
def loan_projection(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount_field', None))
        start_month = int(request.POST.get('smonth_field', None))
        end_month = int(request.POST.get('emonth_field', None))
        current = amount
        length = end_month-start_month

        # declare empty arrays
        month = [0] * length
        price = [0] * length

        for i in range(1, length):
            month[i] = i
            if i > 3:
                current += current * 0.01
            price[i] = current
            zipped_data = zip(month, price)

        return render(request, 'sample/loan_projection.html', {'data': zipped_data})

    else:
        return render(request, 'sample/loan_projection_form.html')