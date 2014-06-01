# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from core.admin import DetailAdmin, SubcategoryAdmin
from .models import JoinSubcategory, JoinDetail
from .forms import JoinSubcategoryForm


class JoinSubcategoryAdmin(SubcategoryAdmin):
    form = JoinSubcategoryForm

admin.site.register(JoinSubcategory, JoinSubcategoryAdmin)


class JoinDetailAdmin(DetailAdmin):
    pass

admin.site.register(JoinDetail, JoinDetailAdmin)
