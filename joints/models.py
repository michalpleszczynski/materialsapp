from django.db import models

from core.models import Category, Subcategory


class Join(Category):
    pass


class JoinSubcategory(Subcategory):

    class Meta:
        verbose_name = 'Join subcategory'
        verbose_name_plural = 'Join subcategories'