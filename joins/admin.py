from django.contrib import admin

from core.admin import SubcategoryAdmin
from .models import JoinSubcategory


class JoinSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(JoinSubcategory, JoinSubcategoryAdmin)
