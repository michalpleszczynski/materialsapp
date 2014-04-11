from django.db import models

from core.models import Category, Subcategory


class CutSubcategory(Subcategory):

    class Meta:
        verbose_name = 'Cut subcategory'
        verbose_name_plural = 'Cut subcategories'