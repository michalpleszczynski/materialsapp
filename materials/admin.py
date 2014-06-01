# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from core.admin import CategoryAdmin, SubcategoryAdmin, DetailAdmin, DetailSectionInline
from .models import Material, MaterialDetail, MaterialSubcategory
from .forms import MaterialSubcategoryForm


class MaterialAdmin(CategoryAdmin):
    pass

admin.site.register(Material, MaterialAdmin)


class MaterialSubcategoryAdmin(SubcategoryAdmin):
    form = MaterialSubcategoryForm

admin.site.register(MaterialSubcategory, MaterialSubcategoryAdmin)


class MaterialDetailAdmin(DetailAdmin):
    pass

admin.site.register(MaterialDetail, MaterialDetailAdmin)