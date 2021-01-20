from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password

class RegisterForm(ModelForm):
    Email = forms.CharField(widget=forms.EmailInput)
    Username = forms.CharField(max_length=100)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}'}))
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'c-password'}))

    class Meta:
        model = User
        fields = (
            'Username',
            'Email',
            'Password',
            'ConfirmPassword'
        )
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['Email']
        user.username = self.cleaned_data['Username']
        user.password = make_password(self.cleaned_data['Password'])
        if commit:
            user.save()
        
        return user