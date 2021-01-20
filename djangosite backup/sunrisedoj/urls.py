"""sunrisedoj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from sunrisedoj import views
from sunrisedoj.views import *

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^forums/$', ForumsView.as_view(), name='forums'),
    url(r'^profile/(?P<u_id>\d+)/$', ProfileView.as_view(), name='profile')
    # path('admin/', admin.site.urls),
    # path('', views.home_view),
    # path('forums/', views.forums_view),
    # path('register/', views.register_view),
    #path('login/', views.login_view)
]