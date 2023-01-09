from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User, Profile, Favorite, Subscription


class ProfileInline(admin.TabularInline):
    """
    Add profile as inline ui view for user in admin site
    """
    model = Profile


class AccountFavoriteAdmin(admin.TabularInline):
    """
    Add Intermediary for many-to-many relation between user and favorite model
    """
    model = User.user_favorites.through


class SubscriptionInline(admin.TabularInline):
    """
    Add subscription as inline ui view for user in admin site
    """
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
    inlines = [ProfileInline, AccountFavoriteAdmin, SubscriptionInline]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """
    Register favorite in admin site
    """
    inlines = [
        AccountFavoriteAdmin
    ]
