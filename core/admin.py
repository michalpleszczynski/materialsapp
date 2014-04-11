from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from .forms import SubcategoryForm
from .models import SubcategoryImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('name',)
    readonly_fields = ('admin_image', )

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        for field in ('subcategories',):
            if db_field.name == field:
                field_name = ' '.join(field.split())
                kwargs['widget'] = FilteredSelectMultiple(field_name, False)
        return super(CategoryAdmin, self).formfield_for_manytomany(
            db_field, request, **kwargs)


class ImageInline(admin.TabularInline):
    model = SubcategoryImage
    extra = 0
    readonly_fields = ('admin_image', )


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'caption', 'facts', 'video_url')}),
        ('Title Image', {'fields': ('title_image', 'admin_title_image')}),
    )
    readonly_fields = ('admin_title_image', )
    form = SubcategoryForm
    inlines = (ImageInline,)