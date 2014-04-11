from django.contrib import admin

from core.admin import SubcategoryAdmin
from .models import FormSubcategory


class FormSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(FormSubcategory, FormSubcategoryAdmin)