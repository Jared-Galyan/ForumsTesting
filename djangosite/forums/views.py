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

class ThreadList(TemplateView):
    template_name = 'threadlist.html'

    def get(self, request, cate_id, forum):
        subforums = SubForum.objects.all()
        threads = Thread.objects.all()
        forums = Forum.objects.all()
        for forumm in forums:
            if str(forumm) == str(forum):
                forumcorrect = forumm
            else:
                continue 
        args = {'subforums': subforums, 'threads': threads, 'forum': forumcorrect}
        return render(request, self.template_name, args)

class SubForumList(TemplateView):
    template_name = 'threadlist.html'

    def get(self, request, cate_id, forum, subforum):
        subforums = SubForum.objects.all()
        threads = Thread.objects.all()
        for forumm in subforums:
            if str(forumm) == str(subforum):
                forumcorrect = forumm
            else:
                continue
        args = {'subforums': subforums, 'threads': threads, 'forum': forumcorrect}
        return render(request, self.template_name, args)
