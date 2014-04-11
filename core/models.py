from datetime import datetime

from django.templatetags.static import static
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django_extensions.db.models import TimeStampedModel


class BaseManager(models.Manager):
    def active(self):
        return self.get_query_set().filter(active=True)


class BaseModel(TimeStampedModel):
    """
    Abstract base class with timestamp fields: created, modified (inherited)
    and active flag
    """
    active = models.BooleanField("active", default=True, null=False, blank=False)

    objects = BaseManager()

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=30, null=False, blank=False)
    image = models.ImageField(
        null=False, blank=False,
        upload_to=lambda instance, filename: '{0}/{1}/{2}'.format(
            ContentType.objects.get_for_model(instance).model, datetime.now().strftime('%Y/%m/%d'), filename))
    alt_text = models.CharField(max_length=50)
    subcategories = models.ManyToManyField('Subcategory', null=True, blank=True)

    def admin_image(self):
        if self.image:
            return '<img src="%s" />' % static(str(self.image))
        else:
            return ''
    admin_image.allow_tags = True

    def __unicode__(self):
        return self.name


class Subcategory(BaseModel):
    name = models.CharField(max_length=60, null=False, blank=False)
    title_image = models.ImageField(
        null=False, blank=False,
        upload_to=lambda instance, filename: '{0}/{1}/{2}'.format(
            ContentType.objects.get_for_model(instance).model, datetime.now().strftime('%Y/%m/%d'), filename))
    caption = models.CharField(max_length=2000)
    facts = models.CharField(max_length=1000)
    video_url = models.URLField(max_length=255)

    def admin_title_image(self):
        if self.title_image:
            return '<img src="%s" />' % static(str(self.title_image))
        else:
            return ''
    admin_title_image.allow_tags = True

    def __unicode__(self):
        return self.name


class SubcategoryImage(models.Model):
    subcategory = models.ForeignKey(Subcategory, related_name='images')
    image = models.ImageField(
        null=False, blank=False,
        upload_to=lambda instance, filename: '{0}/{1}/{2}'.format(
            ContentType.objects.get_for_model(instance.subcategory).model, datetime.now().strftime('%Y/%m/%d'), filename))
    alt_text = models.CharField(max_length=50)

    def admin_image(self):
        if self.image:
            return '<img src="%s" />' % static(str(self.image))
        else:
            return ''
    admin_image.allow_tags = True