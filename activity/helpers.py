from datetime import datetime, timedelta
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from activity.models import Activity


def create_activity(user, action, target=None):
    """
    Create helper for tracking user activity
    :param user:
    :param action:
    :param target:
    :return:
    """
    now = timezone.now()
    last_minute = now - timedelta(seconds=60)
    similar_activities = Activity.objects.filter(user_id=user.id, action=action, created_at__gte=last_minute)
    if target:
        target_content_type = ContentType.objects.get_for_model(target)
        similar_activities = similar_activities.filter(target_content_type=target_content_type, target_id=target.id)
    if not similar_activities:
        # no existing actions found
        action = Activity(user=user, action=action, target=target)
        action.save()
        return True
    return False
