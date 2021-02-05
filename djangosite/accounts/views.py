from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import asyncio
import asqlite
from uuid import uuid4
from cryptography.fernet import Fernet
from asgiref.sync import async_to_sync, sync_to_async
from accounts.forms import RegisterForm
from django.contrib.auth.models import User

# Create your views here.
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        args = {'user_data': user}

        for role in user.userprofile.roles.all():
            print(role.color)

        return render(request, self.template_name, args)

class RegisterView(TemplateView):
    template_name = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('login')