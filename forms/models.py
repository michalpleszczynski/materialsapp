# coding: utf-8
from __future__ import unicode_literals

from core.models import Subcategory, Detail


class FormSubcategory(Subcategory):

    class Meta:
        verbose_name = 'Form subcategory'
        verbose_name_plural = 'Form subcategories'


class FormDetail(Detail):

    class Meta:
        verbose_name = 'Form detail'
        verbose_name_plural = 'Form details'