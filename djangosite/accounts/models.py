from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.db.models.signals import post_save
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=User)
    bio = models.CharField(max_length=500)
    confirmed = models.IntegerField(default=0)
    pfp = ResizedImageField(size=[128, 128], crop=['middle', 'center'], upload_to='profile-pic', quality=99, blank=True, null=True)
    token = models.CharField(max_length=100000)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)