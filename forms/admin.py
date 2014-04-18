from django.contrib import admin

from core.admin import SubcategoryAdmin, DetailAdmin
from .models import FormDetail, FormSubcategory


class FormSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(FormSubcategory, FormSubcategoryAdmin)


class FormDetailAdmin(DetailAdmin):
    pass

admin.site.register(FormDetail, FormDetailAdmin)