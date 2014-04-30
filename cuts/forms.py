# coding: utf-8
from django.forms import ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple

from core.forms import SubcategoryForm
from .models import CutDetail


class CutSubcategoryForm(SubcategoryForm):
    details = ModelMultipleChoiceField(queryset=CutDetail.objects.active(), label=('Select Details'),
                                       widget=FilteredSelectMultiple(
                                           ('details'),
                                           False,
                                       ))