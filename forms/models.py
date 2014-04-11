from django.db import models

from core.models import Category, Subcategory


class FormSubcategory(Subcategory):

    class Meta:
        verbose_name = 'Form subcategory'
        verbose_name_plural = 'Form subcategories'