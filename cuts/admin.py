from django.contrib import admin

from core.admin import SubcategoryAdmin, DetailAdmin
from .models import CutDetail, CutSubcategory


class CutSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(CutSubcategory, CutSubcategoryAdmin)


class CutDetailAdmin(DetailAdmin):
    pass

admin.site.register(CutDetail, CutDetailAdmin)