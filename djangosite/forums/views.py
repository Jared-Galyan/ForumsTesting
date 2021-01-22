from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import asyncio
import asqlite
from uuid import uuid4
from cryptography.fernet import Fernet
from asgiref.sync import async_to_sync, sync_to_async
from django.contrib.auth.models import User
from forums.models import *

class ForumsView(TemplateView):
    template_name = 'forums.html'

    def get(self, request):
        forums = Forum.objects.all()
        categories = Category.objects.all()
        args = {'forums': forums, 'categories': categories}
        return render(request, self.template_name, args)
