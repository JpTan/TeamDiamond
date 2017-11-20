from django import forms
from dbhandler.models import Payment


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['orNum', 'amount', 'date']
