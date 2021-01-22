from django.conf.urls import url
from forums import views
from forums.views import *

urlpatterns = [
    url(r'^$', ForumsView.as_view()),
]