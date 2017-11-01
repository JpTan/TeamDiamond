from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # idnum = forms.NumberInput(max_length=8)

    # data about the user
    class Meta:
        model = User
        fields = ['email', 'password']
