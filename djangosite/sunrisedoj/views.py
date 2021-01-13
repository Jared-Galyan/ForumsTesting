from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView
from sunrisedoj.forms import RegisterForm

class RegisterView(TemplateView):
    template_name = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
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