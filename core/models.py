import time
from datetime import datetime

from django.db import models

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


class Category(BaseModel):
    name = models.CharField(max_length=30, null=False, blank=False)
    image = models.OneToOneField('Image', null=True, blank=True, on_delete=models.SET_NULL)
    subcategories = models.ManyToManyField('Subcategory', null=True, blank=True, related_name='categories')

    def image_preview(self):
        if self.image:
            return self.image.admin_image()
        else:
            return ''
    image_preview.allow_tags = True

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Subcategory(BaseModel):
    name = models.CharField(max_length=60, null=False, blank=False)
    caption = models.CharField(max_length=500, null=True, blank=True)
    details = models.ManyToManyField('Detail', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Detail(BaseModel):
    name = models.CharField(max_length=60, null=False, blank=False)
    title_image = models.OneToOneField('Image', null=True, blank=True, on_delete=models.SET_NULL)
    caption = models.CharField(max_length=2000)
    facts = models.CharField(max_length=1000)
    video_url = models.URLField(max_length=255, null=True, blank=True)

    def title_image_preview(self):
        if self.title_image:
            return self.title_image.admin_image()
        else:
            return ''
    title_image_preview.allow_tags = True

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class DetailSection(BaseModel):
    label = models.CharField(max_length=30, null=True, blank=True)
    detail = models.ForeignKey(Detail, null=False, blank=False, related_name='sections')

    def __unicode__(self):
        return self.label

    def __str__(self):
        return self.label


class Image(models.Model):
    image = ImageField(
        null=False, blank=False,
        upload_to=lambda instance, filename: '{0}/{1}'.format(
            datetime.now().strftime('%Y/%m/%d'), filename + '.' + str(int(time.mktime(datetime.now().timetuple())))
        )
    )
    alt_text = models.CharField(max_length=50, null=True, blank=True)
    figcaption = models.CharField('Figure caption', max_length=150, null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)

    def image_name(self):
        return self.image.name

    def __unicode__(self):
        return self.image.name

    def __str__(self):
        return self.image.name


class DetailSectionImage(Image):
    subcategory = models.ForeignKey(DetailSection, related_name='images')