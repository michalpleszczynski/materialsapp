from django.contrib import admin

from core.admin import CategoryAdmin, SubcategoryAdmin
from .models import Form, FormSubcategory


class FormAdmin(CategoryAdmin):
    pass

admin.site.register(Form, FormAdmin)


class FormSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(FormSubcategory, FormSubcategoryAdmin)