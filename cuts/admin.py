from django.contrib import admin

from core.admin import SubcategoryAdmin
from .models import CutSubcategory


class CutSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(CutSubcategory, CutSubcategoryAdmin)