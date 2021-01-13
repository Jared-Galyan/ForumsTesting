from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from sunrisedoj.forms import RegisterForm
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


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

class RegisterView(TemplateView):
    template_name = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            em = form.cleaned_data['Email']
            un = form.cleaned_data['Username']
            pas = form.cleaned_data['Password']
            print(em)
            result = AsyncStuff.registered(em)
            if result is not None:
                return redirect('login')
            else:
                AsyncStuff.new_account(email=em, username=un, password=pas)
                request.session["user"] = un
                request.session["email"] = em
                return redirect('login')

            return redirect('home')



# def home_view(request):
#     """Home view callable, for the home page."""
#     return render(request, 'index.html')

# def forums_view(request):
#     return render(request, 'forums.html')





# def register_view(request):
#     return render(request, 'register.html')

# def login_view(request):
#     return render(request, 'login.html')