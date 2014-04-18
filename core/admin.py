from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core import urlresolvers

from .forms import SubcategoryForm, DetailForm
from .models import DetailSection, Image, DetailSectionImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('name',)
    readonly_fields = ('image_preview', )

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        for field in ('subcategories',):
            if db_field.name == field:
                field_name = ' '.join(field.split())
                kwargs['widget'] = FilteredSelectMultiple(field_name, False)
        return super(CategoryAdmin, self).formfield_for_manytomany(
            db_field, request, **kwargs)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('name',)
    form = SubcategoryForm

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        for field in ('details',):
            if db_field.name == field:
                field_name = ' '.join(field.split())
                kwargs['widget'] = FilteredSelectMultiple(field_name, False)
        return super(SubcategoryAdmin, self).formfield_for_manytomany(
            db_field, request, **kwargs)


class DetailSectionInline(admin.TabularInline):
    model = DetailSection
    extra = 0
    fields = ('label', 'changeform_link')
    readonly_fields = ('changeform_link',)

    def changeform_link(self, instance):
        if instance.id:
            changeform_url = urlresolvers.reverse(
                'admin:core_detailsection_change', args=(instance.id,)
            )
            return u'<a href="%s" target="_blank">Details</a>' % changeform_url
        return u''
    changeform_link.allow_tags = True
    changeform_link.short_description = ''   # omit column header


class DetailSectionImageInline(admin.StackedInline):
    model = DetailSectionImage
    extra = 0


class DetailSectionAdmin(admin.ModelAdmin):
    inlines = (DetailSectionImageInline,)

admin.site.register(DetailSection, DetailSectionAdmin)


class DetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'caption', 'facts', 'video_url')}),
        ('Title Image', {'fields': ('title_image', 'title_image_preview')}),
    )
    readonly_fields = ('title_image_preview', )
    form = DetailForm
    inlines = (DetailSectionInline,)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_name',)

admin.site.register(Image, ImageAdmin)