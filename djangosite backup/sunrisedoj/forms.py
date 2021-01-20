from django import forms

class RegisterForm(forms.Form):
    Email = forms.CharField()
    Username = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}'}))
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'c-password'}))

class LoginForm(forms.Form):
    Email = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput())