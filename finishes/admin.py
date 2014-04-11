from django.contrib import admin

from core.admin import SubcategoryAdmin
from .models import FinishSubcategory


class FinishSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(FinishSubcategory, FinishSubcategoryAdmin)