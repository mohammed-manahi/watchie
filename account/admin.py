from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User, Profile, Favorite, Subscription


class ProfileInline(admin.TabularInline):
    model = Profile


class FavoriteInline(admin.TabularInline):
    model = Favorite.user.through


class SubscriptionInline(admin.TabularInline):
    model = Subscription


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Register customized user in admin site
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
    inlines = [
        ProfileInline, FavoriteInline, SubscriptionInline
    ]
