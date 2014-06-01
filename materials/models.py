# coding: utf-8
from __future__ import unicode_literals

from core.models import Category, Detail, Subcategory


class Material(Category):
    pass


class MaterialSubcategory(Subcategory):

    class Meta:
        verbose_name = 'Material subcategory'
        verbose_name_plural = 'Material subcategories'


class MaterialDetail(Detail):

    class Meta:
        verbose_name = 'Material detail'
        verbose_name_plural = 'Material details'