from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import asyncio
import asqlite
from uuid import uuid4
from cryptography.fernet import Fernet
from asgiref.sync import async_to_sync, sync_to_async

# Create your views here.
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request):
        return render(request, self.template_name)