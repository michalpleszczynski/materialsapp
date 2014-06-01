# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from core.admin import SubcategoryAdmin, DetailAdmin
from .models import FinishDetail, FinishSubcategory
from .forms import FinishSubcategoryForm


class FinishSubcategoryAdmin(SubcategoryAdmin):
    form = FinishSubcategoryForm

admin.site.register(FinishSubcategory, FinishSubcategoryAdmin)


class FinishDetailAdmin(DetailAdmin):
    pass

admin.site.register(FinishDetail, FinishDetailAdmin)