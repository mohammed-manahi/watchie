from django.contrib import admin
from activity.models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """
    Register action model in admin site
    """
    list_display = ['user', 'action', 'target', 'created_at']
    list_filter = ['created_at']
    search_fields = ['action']
