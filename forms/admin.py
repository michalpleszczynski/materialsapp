# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from core.admin import SubcategoryAdmin, DetailAdmin
from .models import FormDetail, FormSubcategory


class FormSubcategoryAdmin(SubcategoryAdmin):

    def get_form(self, request, obj=None, **kwargs):
        from . import DETAIL_TYPE
        form = super(FormSubcategoryAdmin, self).get_form(request, obj, **kwargs)
        if 'category' in form.base_fields:
            field = form.base_fields['category']
            field.queryset = field.queryset.filter(type=DETAIL_TYPE)
        return form

admin.site.register(FormSubcategory, FormSubcategoryAdmin)


class FormDetailAdmin(DetailAdmin):

    def get_form(self, request, obj=None, **kwargs):
        from . import DETAIL_TYPE
        form = super(FormDetailAdmin, self).get_form(request, obj, **kwargs)
        if 'subcategory' in form.base_fields:
            field = form.base_fields['subcategory']
            field.queryset = field.queryset.filter(type=DETAIL_TYPE)
        return form

admin.site.register(FormDetail, FormDetailAdmin)