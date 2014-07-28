# coding: utf-8
from __future__ import unicode_literals

from core.models import BaseManager, Subcategory, Detail
from . import DETAIL_TYPE


class CutTypeManager(BaseManager):

    def get_queryset(self):
        q = super(CutTypeManager, self).get_queryset()
        return q.filter(type=DETAIL_TYPE)


class CutSubcategory(Subcategory):

    objects = CutTypeManager()

    class Meta:
        proxy = True
        verbose_name = 'Cut subcategory'
        verbose_name_plural = 'Cut subcategories'

    def save(self, *args, **kwargs):
        self.type = DETAIL_TYPE
        super(CutSubcategory, self).save(*args, **kwargs)


class CutDetail(Detail):

    objects = CutTypeManager()

    class Meta:
        proxy = True
        verbose_name = 'Cut detail'
        verbose_name_plural = 'Cut details'

    def save(self, *args, **kwargs):
        self.type = DETAIL_TYPE
        super(CutDetail, self).save(*args, **kwargs)