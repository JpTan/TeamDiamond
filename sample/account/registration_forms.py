from .models import Student
from django import forms


class RegistrationUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'id_number', 'email', 'college', 'course', 'cellphone_number', 'password']
