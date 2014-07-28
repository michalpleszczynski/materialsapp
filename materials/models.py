# coding: utf-8
from __future__ import unicode_literals

from core.models import BaseManager, Category, Detail, Subcategory
from . import DETAIL_TYPE


class MaterialTypeManager(BaseManager):

    def get_queryset(self):
        q = super(MaterialTypeManager, self).get_queryset()
        return q.filter(type=DETAIL_TYPE)


class Material(Category):

    class Meta:
        proxy = True


class MaterialSubcategory(Subcategory):

    objects = MaterialTypeManager()

    class Meta:
        proxy = True
        verbose_name = 'Material subcategory'
        verbose_name_plural = 'Material subcategories'

    def save(self, *args, **kwargs):
        self.type = DETAIL_TYPE
        super(MaterialSubcategory, self).save(*args, **kwargs)


class MaterialDetail(Detail):

    objects = MaterialTypeManager()

    class Meta:
        proxy = True
        verbose_name = 'Material detail'
        verbose_name_plural = 'Material details'

    def save(self, *args, **kwargs):
        self.type = DETAIL_TYPE
        super(MaterialDetail, self).save(*args, **kwargs)