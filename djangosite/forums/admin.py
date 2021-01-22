from django.contrib import admin
from forums.models import *

admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Reply)
admin.site.register(Category)
