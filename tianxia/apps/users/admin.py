from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

class OrdernaryUserInline(admin.TabularInline):
    model = OrdernaryUser
    can_delete = False
    verbose_name_plural = '普通会员表'

class UserAdmin(BaseUserAdmin):
    inlines=(OrdernaryUserInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(ArticalType)
admin.site.register(ArticalDetails)
