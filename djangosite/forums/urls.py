from django.conf.urls import url
from forums import views
from forums.views import *

urlpatterns = [
    url(r'^$', ForumsView.as_view()),
    url(r'^(?P<cate_id>\d+)/(?P<forum>[-\w]+)/$', ThreadList.as_view()),
    url(r'^(?P<cate_id>\d+)/(?P<forum>[-\w]+)/(?P<thread_id>\d+)/$', ThreadList.as_view()),
    url(r'^(?P<cate_id>\d+)/(?P<forum>[-\w]+)/(?P<subforum>[-\w]+)/$', SubForumList.as_view()),
    url(r'^(?P<cate_id>\d+)/(?P<forum>[-\w]+)/(?P<subforum>[-\w]+)/(?P<thread_id>\d+)/$', ThreadList.as_view())
]