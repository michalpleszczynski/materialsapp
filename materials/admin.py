# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from core.admin import CategoryAdmin, SubcategoryAdmin, DetailAdmin
from .models import Material, MaterialDetail, MaterialSubcategory

admin.site.register(Material, CategoryAdmin)


class MaterialSubcategoryAdmin(SubcategoryAdmin):

    def get_form(self, request, obj=None, **kwargs):
        from . import DETAIL_TYPE
        form = super(MaterialSubcategoryAdmin, self).get_form(request, obj, **kwargs)
        if 'category' in form.base_fields:
            field = form.base_fields['category']
            field.queryset = field.queryset.filter(type=DETAIL_TYPE)
            field.required = True
        return form

admin.site.register(MaterialSubcategory, MaterialSubcategoryAdmin)


class MaterialDetailAdmin(DetailAdmin):

    def get_form(self, request, obj=None, **kwargs):
        from . import DETAIL_TYPE
        form = super(MaterialDetailAdmin, self).get_form(request, obj, **kwargs)
        if 'subcategory' in form.base_fields:
            field = form.base_fields['subcategory']
            field.queryset = field.queryset.filter(type=DETAIL_TYPE)
        return form

admin.site.register(MaterialDetail, MaterialDetailAdmin)