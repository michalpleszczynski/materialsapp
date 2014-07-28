# coding: utf-8
from __future__ import unicode_literals

from core.models import BaseManager, Subcategory, Detail
from . import DETAIL_TYPE


class FormsTypeManager(BaseManager):

    def get_queryset(self):
        q = super(FormsTypeManager, self).get_queryset()
        return q.filter(type=DETAIL_TYPE)


class FormSubcategory(Subcategory):

    objects = FormsTypeManager()

    class Meta:
        proxy = True
        verbose_name = 'Form subcategory'
        verbose_name_plural = 'Form subcategories'

    def save(self, *args, **kwargs):
        self.type = DETAIL_TYPE
        super(FormSubcategory, self).save(*args, **kwargs)


class FormDetail(Detail):

    objects = FormsTypeManager()

    class Meta:
        proxy = True
        verbose_name = 'Form detail'
        verbose_name_plural = 'Form details'

    def save(self, *args, **kwargs):
        self.type = DETAIL_TYPE
        super(FormDetail, self).save(*args, **kwargs)