from django.contrib import admin
from accounts.models import *

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(RolePermissions)
admin.site.register(UserRoles)
admin.site.site_header = 'SunriseDOJ Admin Panel'