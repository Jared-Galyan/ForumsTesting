from django.contrib import admin
from forums.models import *

admin.site.register(Category)
admin.site.register(Forum)
admin.site.register(SubForum)
admin.site.register(Thread)
admin.site.register(Reply)

