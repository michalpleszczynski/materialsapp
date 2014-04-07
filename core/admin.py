from django.contrib import admin

from .forms import SubcategoryForm
from .models import SubcategoryImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    readonly_fields = ('admin_image', )


class ImageInline(admin.TabularInline):
    model = SubcategoryImage
    extra = 0
    readonly_fields = ('admin_image', )


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'caption', 'facts', 'video_url')}),
        ('Title Image', {'fields': ('title_image', 'admin_title_image')}),
    )
    readonly_fields = ('admin_title_image', )
    form = SubcategoryForm
    inlines = (ImageInline,)