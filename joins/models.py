# coding: utf-8
from __future__ import unicode_literals

from core.models import Subcategory, Detail


class JoinSubcategory(Subcategory):

    class Meta:
        verbose_name = 'Join subcategory'
        verbose_name_plural = 'Join subcategories'


class JoinDetail(Detail):

    class Meta:
        verbose_name = 'Join detail'
        verbose_name_plural = 'Join details'