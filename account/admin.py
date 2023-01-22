from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User, Profile, Subscription


class ProfileInline(admin.TabularInline):
    """
    Add profile model as inline ui view for user in admin site
    """
    model = Profile


class SubscriptionInline(admin.TabularInline):
    """
    Add subscription model as inline ui view for user in admin site
    """
    model = Subscription


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Register customized user model in admin site
    """
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                # Add email, first name and last name fields to default fields
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )
    inlines = [ProfileInline, SubscriptionInline]



