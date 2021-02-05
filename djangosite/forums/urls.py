from django.conf.urls import url
from django.urls import path, include
from forums import views
from forums.views import *

from machina import urls as machina_urls

urlpatterns = [
    # [...]
    path('', include(machina_urls)),
]

# urlpatterns = [
#     url(r'^$', ForumsView.as_view()),
#     url(r'^(?P<cate_id>\d+)/(?P<forum>[-\w]+)/$', ThreadList.as_view()),
#     url(r'^(?P<cate_id>\d+)/(?P<forum>[-\w]+)/(?P<thread_id>\d+)/$', ThreadList.as_view()),
#     url(r'^(?P<cate_id>\d+)/(?P<forum>[-\w]+)/(?P<subforum>[-\w]+)/$', SubForumList.as_view()),
#     url(r'^(?P<cate_id>\d+)/(?P<forum>[-\w]+)/(?P<subforum>[-\w]+)/(?P<thread_id>\d+)/$', ThreadList.as_view())
# ]