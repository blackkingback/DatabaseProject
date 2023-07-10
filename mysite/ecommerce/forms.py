from django import forms

class UserRegistrationForm(forms.Form):
    First_name = forms.CharField(label='First_name', max_length=100)
    Last_name = forms.CharField(label='Last_name', max_length=100)
    Email = forms.CharField(label='Email', max_length=100)
    Username = forms.CharField(label='Username', max_length=100)
    Password = forms.CharField(widget=forms.PasswordInput())