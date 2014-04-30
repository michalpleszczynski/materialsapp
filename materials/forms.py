# coding: utf-8
from django.forms import ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple

from core.forms import SubcategoryForm
from .models import MaterialDetail


class MaterialSubcategoryForm(SubcategoryForm):
    details = ModelMultipleChoiceField(queryset=MaterialDetail.objects.active(), label=('Select Details'),
                                       widget=FilteredSelectMultiple(
                                           ('details'),
                                           False,
                                       ))