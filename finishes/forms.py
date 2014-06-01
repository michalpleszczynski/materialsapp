# coding: utf-8
from __future__ import unicode_literals

from django.forms import ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple

from core.forms import SubcategoryForm
from .models import FinishDetail


class FinishSubcategoryForm(SubcategoryForm):
    details = ModelMultipleChoiceField(queryset=FinishDetail.objects.active(), label=('Select Details'),
                                       widget=FilteredSelectMultiple(
                                           ('details'),
                                           False,
                                       ))