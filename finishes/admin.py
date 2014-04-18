from django.contrib import admin

from core.admin import SubcategoryAdmin, DetailAdmin
from .models import FinishDetail, FinishSubcategory


class FinishSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(FinishSubcategory, FinishSubcategoryAdmin)


class FinishDetailAdmin(DetailAdmin):
    pass

admin.site.register(FinishDetail, FinishDetailAdmin)