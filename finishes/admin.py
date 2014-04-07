from django.contrib import admin

from core.admin import CategoryAdmin, SubcategoryAdmin
from .models import Finish, FinishSubcategory


class FinishAdmin(CategoryAdmin):
    pass

admin.site.register(Finish, FinishAdmin)


class FinishSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(FinishSubcategory, FinishSubcategoryAdmin)