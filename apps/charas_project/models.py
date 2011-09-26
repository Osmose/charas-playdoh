from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class ModelBase(models.Model):
    """Base class for models across the site."""
    class Meta:
        abstract = True


class FrontPageFeature(ModelBase):
    """Feature story to appear on the front page."""
    author = models.ForeignKey(User, editable=False, null=True, blank=True)

    image = models.ImageField(upload_to=settings.FRONT_PAGE_FEATURE_PATH,
                              max_length=settings.MAX_FILEPATH_LENGTH,
                              null=True,
                              blank=True)
    headline = models.CharField(max_length=255)
    body = models.TextField()
    button_text = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField()

    enabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
