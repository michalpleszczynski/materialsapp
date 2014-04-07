from django.contrib import admin

from core.admin import CategoryAdmin, SubcategoryAdmin
from .models import Cut, CutSubcategory


class CutAdmin(CategoryAdmin):
    pass

admin.site.register(Cut, CutAdmin)


class CutSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(CutSubcategory, CutSubcategoryAdmin)