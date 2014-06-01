# coding: utf-8
from __future__ import unicode_literals

from core.models import Subcategory, Detail


class FinishSubcategory(Subcategory):

    class Meta:
        verbose_name = 'Finish subcategory'
        verbose_name_plural = 'Finish subcategories'


class FinishDetail(Detail):

    class Meta:
        verbose_name = 'Finish detail'
        verbose_name_plural = 'Finish details'