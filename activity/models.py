from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from account.models import User


class Activity(models.Model):
    """
    Create activity model and associate it with user model
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='activities', on_delete=models.CASCADE)
    action = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    target_content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_project',
                                            on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_id')

    class Meta:
        indexes = [models.Index(fields=['created_at']), models.Index(fields=['target_content_type', 'target_id'])]
        ordering = ['-created_at']
