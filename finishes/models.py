from django.db import models

from core.models import Category, Subcategory


class FinishSubcategory(Subcategory):

    class Meta:
        verbose_name = 'Finish subcategory'
        verbose_name_plural = 'Finish subcategories'