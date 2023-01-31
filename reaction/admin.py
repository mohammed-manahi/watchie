from django.contrib import admin
from reaction.models import Reaction


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    """
     Register reaction model in admin site
    """
    list_display = ['like', 'comment']
    list_filter = ['created_at']
    search_fields = ['comment']
