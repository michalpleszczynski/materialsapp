from django.contrib import admin

from core.admin import DetailAdmin, SubcategoryAdmin
from .models import JoinSubcategory, JoinDetail


class JoinSubcategoryAdmin(SubcategoryAdmin):
    pass

admin.site.register(JoinSubcategory, JoinSubcategoryAdmin)


class JoinDetailAdmin(DetailAdmin):
    pass

admin.site.register(JoinDetail, JoinDetailAdmin)
