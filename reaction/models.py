from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from account.models import User


class Reaction(models.Model):
    """
    Create reaction model and associate it with user model using many-to-many relationship
    """
    users_reactions = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reactions', blank=True)
    like = models.BooleanField(default=0, blank=True)
    comment = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    target_content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_stream',
                                            on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_id')

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_comments(self):
        return self.comments.count()

    class Meta:
        indexes = [models.Index(fields=["-created_at"]), ]
        ordering = ["-created_at"]
