from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from sunrisedoj.forms import *
import asyncio
import asqlite
from uuid import uuid4
from cryptography.fernet import Fernet
from asgiref.sync import async_to_sync, sync_to_async

key = b'alerr8icGEY6tbt3qvLWg5hJU6C_BIeCIQ5_zZzwWOM='
cipher_suite = Fernet(key)

class AsyncStuff():
    @async_to_sync
    async def registered(self, email):
        print(email)
        async with asqlite.connect("djangosite/main.db") as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("SELECT email FROM users WHERE email = '{}'".format(email))
                result = await cursor.fetchone()
        return result
    
    @async_to_sync
    async def new_account(self, email, username, password):
        auth_token = uuid4()
        pas = cipher_suite.encrypt(bytes(password, encoding='utf8'))
        sql = ("INSERT INTO users(email, username, password, confirmed, pfp, bio, perms, friends, token) VALUES(?,?,?,?,?,?,?,?,?)")
        val = (str(email),str(username), pas, False, "N/A", "N/A", "N/A", "N/A", str(auth_token))
        async with asqlite.connect("djangosite/main.db") as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql, val)
        return
    
    @async_to_sync
    async def login(self, email):
        async with asqlite.connect("djangosite/main.db") as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("SELECT email, username, password, confirmed FROM users WHERE email = '{}'".format(email))
                result = await cursor.fetchone()
        return result


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        if 'user' in request.session:
            sessiondata = {'user': request.session['user'], 'email': request.session['email']}
            return render(request, self.template_name, sessiondata)
        else:
            return render(request, self.template_name)

class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request):
        if 'user' in request.session:
            return redirect('home')
        else:
            form = LoginForm()
            return render(request, self.template_name, {'form': form})
        
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            em = form.cleaned_data['Email']
            pas = form.cleaned_data['Password']
            result = AsyncStuff.login(email=em)
            if result is None:
                return redirect('login')
            elif bytes(pas, encoding='utf8') != cipher_suite.decrypt(result[2]):
                return redirect('login')
            else:
                if int(result[3]) == 1:
                    request.session["user"] = str(result[1])
                    request.session["email"] = str(result[0])
                    return redirect('home')
                else:
                    return render('need_confirmed.html')

# def home_view(request):
#     """Home view callable, for the home page."""
#     return render(request, 'index.html')

# def forums_view(request):
#     return render(request, 'forums.html')





# def register_view(request):
#     return render(request, 'register.html')

# def login_view(request):
#     return render(request, 'login.html')