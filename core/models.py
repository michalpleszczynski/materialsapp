# coding: utf-8
from __future__ import unicode_literals
import time
from datetime import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django_extensions.db.models import TimeStampedModel
from sorl.thumbnail import ImageField


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


class TypeManager(BaseManager):

    def cuts(self):
        from cuts import DETAIL_TYPE
        return self.active().filter(type=DETAIL_TYPE)

    def finishes(self):
        from finishes import DETAIL_TYPE
        return self.active().filter(type=DETAIL_TYPE)

    def joins(self):
        from joins import DETAIL_TYPE
        return self.active().filter(type=DETAIL_TYPE)

    def forms(self):
        from forms import DETAIL_TYPE
        return self.active().filter(type=DETAIL_TYPE)

    def materials(self):
        from materials import DETAIL_TYPE
        return self.active().filter(type=DETAIL_TYPE)


@python_2_unicode_compatible
class Category(BaseModel):
    name = models.CharField(max_length=30, null=False, blank=False)
    image = models.OneToOneField('Image', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=15, null=False, blank=True)

    objects = TypeManager()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Subcategory(BaseModel):
    name = models.CharField(max_length=60, null=False, blank=False)
    caption = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    type = models.CharField(max_length=15, null=False, blank=True)

    objects = TypeManager()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Detail(BaseModel):
    name = models.CharField(max_length=60, null=False, blank=False)
    title_image = models.OneToOneField('Image', null=True, blank=False, on_delete=models.SET_NULL)
    caption = models.CharField(max_length=2000)
    facts = models.CharField(max_length=1000)
    video_url = models.URLField(max_length=255, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, related_name='details')
    type = models.CharField(max_length=15, null=False, blank=True)

    objects = TypeManager()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class DetailSection(BaseModel):
    label = models.CharField(max_length=30, null=True, blank=True)
    detail = models.ForeignKey(Detail, null=False, blank=False, related_name='sections')

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Image(models.Model):
    image = ImageField(
        null=False, blank=False, max_length=255,
        upload_to=lambda instance, filename: '{0}/{1}'.format(
            datetime.now().strftime('%Y/%m/%d'), filename + '.' + str(int(time.mktime(datetime.now().timetuple())))
        )
    )
    alt_text = models.CharField(max_length=50, null=True, blank=True)
    figcaption = models.CharField('Figure caption', max_length=150, null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.image.name


class DetailSectionImage(Image):
    subcategory = models.ForeignKey(DetailSection, related_name='images')