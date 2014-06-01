# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from core.admin import SubcategoryAdmin, DetailAdmin
from .models import FormDetail, FormSubcategory
from .forms import FormSubcategoryForm


class FormSubcategoryAdmin(SubcategoryAdmin):
    form = FormSubcategoryForm

admin.site.register(FormSubcategory, FormSubcategoryAdmin)


class FormDetailAdmin(DetailAdmin):
    pass

admin.site.register(FormDetail, FormDetailAdmin)