from django.contrib import admin

from core.admin import CategoryAdmin, SubcategoryAdmin
from .models import Join, JoinSubcategory


class JoinAdmin(CategoryAdmin):
    pass

admin.site.register(Join, JoinAdmin)


class JoinSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(JoinSubcategory, JoinSubcategoryAdmin)
