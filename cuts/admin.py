# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from core.admin import SubcategoryAdmin, DetailAdmin
from .models import CutDetail, CutSubcategory
from .forms import CutSubcategoryForm


class CutSubcategoryAdmin(SubcategoryAdmin):
    form = CutSubcategoryForm

admin.site.register(CutSubcategory, CutSubcategoryAdmin)


class CutDetailAdmin(DetailAdmin):
    pass

admin.site.register(CutDetail, CutDetailAdmin)