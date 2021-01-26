from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from sunrisedoj.forms import *
import asyncio
import asqlite
from asgiref.sync import async_to_sync, sync_to_async


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        if 'user' in request.session:
            sessiondata = {'user': request.session['user'], 'email': request.session['email']}
            return render(request, self.template_name, sessiondata)
        else:
            return render(request, self.template_name)

# def home_view(request):
#     """Home view callable, for the home page."""
#     return render(request, 'index.html')

# def forums_view(request):
#     return render(request, 'forums.html')





# def register_view(request):
#     return render(request, 'register.html')

# def login_view(request):
#     return render(request, 'login.html')