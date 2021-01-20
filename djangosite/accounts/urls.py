from django.conf.urls import url
from accounts import views
from accounts.views import *
from django.contrib.auth.views import LoginView
from django.contrib import admin

urlpatterns = [
    url(r'^$', ProfileView.as_view()),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^admin/', admin.site.urls)
]