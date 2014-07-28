# coding: utf-8
from __future__ import unicode_literals

from core.models import BaseManager, Subcategory, Detail
from . import DETAIL_TYPE


class FinishTypeManager(BaseManager):

    def get_queryset(self):
        q = super(FinishTypeManager, self).get_queryset()
        return q.filter(type=DETAIL_TYPE)


class FinishSubcategory(Subcategory):

    objects = FinishTypeManager()

    class Meta:
        proxy = True
        verbose_name = 'Finish subcategory'
        verbose_name_plural = 'Finish subcategories'

    def save(self, *args, **kwargs):
        self.type = DETAIL_TYPE
        super(FinishSubcategory, self).save(*args, **kwargs)


class FinishDetail(Detail):

    objects = FinishTypeManager()

    class Meta:
        proxy = True
        verbose_name = 'Finish detail'
        verbose_name_plural = 'Finish details'

    def save(self, *args, **kwargs):
        self.type = DETAIL_TYPE
        super(FinishDetail, self).save(*args, **kwargs)