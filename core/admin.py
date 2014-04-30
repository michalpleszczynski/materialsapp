from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple, RelatedFieldWidgetWrapper
from django.core import urlresolvers

from sorl.thumbnail.admin import AdminImageMixin

from .forms import SubcategoryForm, DetailForm
from .models import DetailSection, Image, DetailSectionImage, Detail, Category
from .widgets import AdminRelatedImageWidget


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('name',)
    change_form_template = 'admin/change_form_with_image.html'

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        for field in ('subcategories',):
            if db_field.name == field:
                field_name = ' '.join(field.split())
                kwargs['widget'] = FilteredSelectMultiple(field_name, False)
        return super(CategoryAdmin, self).formfield_for_manytomany(
            db_field, request, **kwargs)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            return db_field.formfield(widget=
                                      RelatedFieldWidgetWrapper(
                                          AdminRelatedImageWidget(),
                                          Category._meta.get_field('image').rel,
                                          self.admin_site
                                      ))
        sup = super(CategoryAdmin, self)
        return sup.formfield_for_dbfield(db_field, **kwargs)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('name',)


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


class DetailSectionImageInline(AdminImageMixin, admin.StackedInline):
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
        ('Title Image', {'fields': ('title_image',)}),
    )
    form = DetailForm
    inlines = (DetailSectionInline,)
    change_form_template = 'admin/change_form_with_image.html'

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'title_image':
            return db_field.formfield(widget=
                                      RelatedFieldWidgetWrapper(
                                          AdminRelatedImageWidget(),
                                          Detail._meta.get_field('title_image').rel,
                                          self.admin_site
                                      ))
        sup = super(DetailAdmin, self)
        return sup.formfield_for_dbfield(db_field, **kwargs)


class ImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('image_name',)

admin.site.register(Image, ImageAdmin)