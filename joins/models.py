# coding: utf-8
from __future__ import unicode_literals

from core.models import BaseManager, Subcategory, Detail
from . import DETAIL_TYPE


class JoinTypeManager(BaseManager):

    def get_queryset(self):
        q = super(JoinTypeManager, self).get_queryset()
        return q.filter(type=DETAIL_TYPE)


class JoinSubcategory(Subcategory):

    objects = JoinTypeManager()

    class Meta:
        proxy = True
        verbose_name = 'Join subcategory'
        verbose_name_plural = 'Join subcategories'

    def save(self, *args, **kwargs):
        self.type = DETAIL_TYPE
        super(JoinSubcategory, self).save(*args, **kwargs)


class JoinDetail(Detail):

    objects = JoinTypeManager()

    class Meta:
        proxy = True
        verbose_name = 'Join detail'
        verbose_name_plural = 'Join details'

    def save(self, *args, **kwargs):
        self.type = DETAIL_TYPE
        super(JoinDetail, self).save(*args, **kwargs)