from django.db import models

from core.models import Category, Subcategory


class Material(Category):
    pass


class MaterialSubcategory(Subcategory):

    class Meta:
        verbose_name = 'Material subcategory'
        verbose_name_plural = 'Material subcategories'