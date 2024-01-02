from django.contrib import admin
from .model import UserProfile, Account


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'username', 'phone_number')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
