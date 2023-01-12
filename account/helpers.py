from django.utils import timezone
from account.models import User, Subscription


def is_subscription_active(pk):
    """
    Create helper method to check subscription
    :param pk:
    :return subscription status:
    """
    now = timezone.now()
    try:
        return bool(Subscription.objects.get(valid_from__lte=now, valid_to__gte=now, active=True, user__pk=pk))
    except Subscription.DoesNotExist:
        return False
