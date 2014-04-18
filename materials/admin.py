from django.contrib import admin

from core.admin import CategoryAdmin, SubcategoryAdmin, DetailAdmin, DetailSectionInline
from .models import Material, MaterialDetail, MaterialSubcategory


class MaterialAdmin(CategoryAdmin):
    pass

admin.site.register(Material, MaterialAdmin)


class MaterialSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(MaterialSubcategory, MaterialSubcategoryAdmin)


class MaterialDetailAdmin(DetailAdmin):
    pass

admin.site.register(MaterialDetail, MaterialDetailAdmin)