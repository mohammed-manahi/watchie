from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User, Profile, Subscription


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a signal for user profile
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return create user profile:
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Save user profile
    :param sender:
    :param instance:
    :param kwargs:
    :return save user profile:
    """
    instance.profile.save()


@receiver(post_save, sender=User)
def create_user_subscription(sender, instance, created, **kwargs):
    """
    Create user subscription
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return create user subscription:
    """
    # Get default value for field subscription type in subscription model
    subscription_code = Subscription._meta.get_field('code').get_default()
    subscription_type = Subscription._meta.get_field('type').get_default()
    subscription_start = timezone.now()
    subscription_end = timezone.now() + timedelta(days=14)
    if created:
        Subscription.objects.create(user=instance, code=subscription_code, type=subscription_type,
                                    valid_from=subscription_start, valid_to=subscription_end, active=True)


@receiver(post_save, sender=User)
def save_user_subscription(sender, instance, **kwargs):
    """
    Save user subscription
    :param sender:
    :param instance:
    :param kwargs:
    :return save user subscription:
    """
    instance.subscription.save()