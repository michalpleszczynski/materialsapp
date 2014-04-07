from django.contrib import admin

from core.admin import CategoryAdmin, SubcategoryAdmin
from .models import Material, MaterialSubcategory


class MaterialAdmin(CategoryAdmin):
    pass

admin.site.register(Material, MaterialAdmin)


class MaterialSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(MaterialSubcategory, MaterialSubcategoryAdmin)