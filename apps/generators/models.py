import Image
from base64 import b64encode
from StringIO import StringIO

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Generator(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Generator Name')
    slug = models.SlugField()

    resource_width = models.IntegerField()
    resource_height = models.IntegerField()

    preview_width = models.IntegerField()
    preview_height = models.IntegerField()
    preview_x = models.IntegerField()
    preview_y = models.IntegerField()

    def __unicode__(self):
        return u'Generator: %s' % self.name


class Part(models.Model):
    generator = models.ForeignKey(Generator, verbose_name=u'Generator')
    name = models.CharField(max_length=255, verbose_name=u'Part Name')
    slug = models.SlugField()
    order = models.IntegerField()

    def __unicode__(self):
        return u'%s: %s' % (self.generator.name, self.name)


class Resource(models.Model):
    part = models.ForeignKey(Part, verbose_name=u'Part')
    user = models.ForeignKey(User, verbose_name=u'Creator')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    approved = models.BooleanField(default=False, verbose_name=u'Approved')
    color = models.CharField(max_length=255, verbose_name=u'Color')

    resource = models.ImageField(upload_to=settings.GENERATOR_RESOURCE_PATH,
                                 verbose_name=u'Resource',
                                 max_length=settings.MAX_FILEPATH_LENGTH)

    preview = models.TextField(editable=False)

    def save(self, *args, **kwargs):
        """Generate preview and save as base64 png on save."""

        img = Image.open(self.resource.file)
        gen = self.part.generator
        preview = img.crop((gen.preview_x,
                            gen.preview_y,
                            gen.preview_x + gen.preview_width,
                            gen.preview_y + gen.preview_height))

        f = StringIO()
        preview.save(f, 'PNG')
        self.preview = 'data:image/png;base64,' + b64encode(f.getvalue())

        super(Resource, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s: %s' % (self.part, self.pk)
