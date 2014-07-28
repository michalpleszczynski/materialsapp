# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from core.admin import DetailAdmin, SubcategoryAdmin
from .models import JoinSubcategory, JoinDetail


class JoinSubcategoryAdmin(SubcategoryAdmin):

    def get_form(self, request, obj=None, **kwargs):
        from . import DETAIL_TYPE
        form = super(JoinSubcategoryAdmin, self).get_form(request, obj, **kwargs)
        if 'category' in form.base_fields:
            field = form.base_fields['category']
            field.queryset = field.queryset.filter(type=DETAIL_TYPE)
        return form

admin.site.register(JoinSubcategory, JoinSubcategoryAdmin)


class JoinDetailAdmin(DetailAdmin):

    def get_form(self, request, obj=None, **kwargs):
        from . import DETAIL_TYPE
        form = super(JoinDetailAdmin, self).get_form(request, obj, **kwargs)
        if 'subcategory' in form.base_fields:
            field = form.base_fields['subcategory']
            field.queryset = field.queryset.filter(type=DETAIL_TYPE)
        return form

admin.site.register(JoinDetail, JoinDetailAdmin)
