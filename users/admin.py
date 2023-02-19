from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import SocialUser


class SocialUserInline(admin.StackedInline):
    model = SocialUser
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (SocialUserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
