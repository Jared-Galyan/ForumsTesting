from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=150, default='None')
    ordering = models.IntegerField(blank=True, null=True)
    perms = models.CharField(max_length=500, default='None', null=True)

    def __str__(self):
        return self.name

class Forum(models.Model):
    category = models.ForeignKey(Category, on_delete=Category, null=True)
    name = models.CharField(max_length=150)
    parent = models.BooleanField(default=False)
    description = models.CharField(max_length=500)
    threads = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
    ordering = models.IntegerField(blank=True, null=True)
    latest_thread_time = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Thread(models.Model):
    forum = models.ForeignKey(Forum, on_delete=Forum)
    name = models.CharField(max_length=150)
    content = models.CharField(max_length=1000)
    labels = models.CharField(max_length=500)
    viewed = models.CharField(max_length=500)
    author = models.OneToOneField(User, on_delete=User)
    closed = models.BooleanField(blank=True, default=False)
    latest_post_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=Thread)
    content = models.CharField(max_length=1000)
    viewed = models.CharField(max_length=500)
    author = models.OneToOneField(User, on_delete=User)
