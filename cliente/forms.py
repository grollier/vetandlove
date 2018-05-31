from django import forms
from django.contrib.auth.forms import UserCreationForm

class FormPassConfirmation(UserCreationForm):
    username = forms.CharField(
         widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password1 = forms.CharField(
         widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    password2 = forms.CharField(
         widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
