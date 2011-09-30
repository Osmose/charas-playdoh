from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

from gamemakers import GAMEMAKER_CHOICES

from charas_project.models import ModelBase


RESOURCE_TYPES = [
    (1, 'image'),
    (2, 'music'),
]


class Category(ModelBase):
    name = models.CharField(max_length=255)
    maker = models.SlugField(choices=GAMEMAKER_CHOICES)
    resource_type = models.PositiveIntegerField(choices=RESOURCE_TYPES)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Resource(ModelBase):
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User, related_name='cr_resource_set')

    name = models.CharField(max_length=255)
    description = models.TextField()
    upload = models.FileField(upload_to=settings.CR_RESOURCE_PATH,
                              max_length=settings.MAX_FILEPATH_LENGTH)
    approved = models.BooleanField(default=False)
