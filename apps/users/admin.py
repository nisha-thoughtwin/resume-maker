from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import *


class UserInline(admin.StackedInline):
    model = User


class UserAdmin(admin.ModelAdmin):
    # inlines = [
    #     UserInline,
    # ]
    list_display = ["username", "account_approved","parent","is_teamleader"]


admin.site.register(User, UserAdmin)
