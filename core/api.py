# coding: utf-8
from __future__ import unicode_literals

from tastypie import fields
from tastypie import http
from tastypie.resources import ModelResource
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.paginator import Paginator
from sorl.thumbnail.shortcuts import get_thumbnail

from .models import Category, Subcategory, Detail, Image, DetailSection
from .mixins import DropNullMixin, DetailMixin
from . import (CATEGORY_THUMB_PARAMS, SUBCATEGORY_THUMB_PARAMS,
               DETAIL_SECTION_THUMB_PARAMS, DETAIL_FULL_IMAGE)


class NoMetaPaginator(Paginator):
    """
    Paginator with no meta.
    """
    def page(self):
        res = super(NoMetaPaginator, self).page()
        del res['meta']
        return res


class BaseModelResource(ModelResource):

    class Meta:
        include_resource_uri = False
        paginator_class = NoMetaPaginator


class ImageResource(DropNullMixin, BaseModelResource):

    thumb_params = None

    class Meta(BaseModelResource.Meta):
        allowed_methods = []
        fields = ('alt_text', 'figcaption', 'url')
        queryset = Image.objects.all()

    def dehydrate(self, bundle):
        bundle = super(ImageResource, self).dehydrate(bundle)
        if self.thumb_params:
            thumb = get_thumbnail(bundle.obj.image, **self.thumb_params)
            bundle.data.update({
                'thumb': thumb.url,
                'full_image': bundle.obj.image.url
            })
        return bundle


class CategoryImageResource(ImageResource):
    thumb_params = CATEGORY_THUMB_PARAMS


class SubcategoryImageResource(ImageResource):
    thumb_params = SUBCATEGORY_THUMB_PARAMS


class DetailImageResource(ImageResource):
    thumb_params = DETAIL_FULL_IMAGE


class DetailSectionImageResource(ImageResource):
    thumb_params = DETAIL_SECTION_THUMB_PARAMS


class CategoryResource(BaseModelResource):

    image = fields.ToOneField(CategoryImageResource, 'image', full=True)

    class Meta(BaseModelResource.Meta):
        resource_name = 'categories'
        collection_name = resource_name
        allowed_methods = ['get']
        queryset = Category.objects.active().select_related('image')
        fields = ('id', 'name', 'type')
        filtering = {
            'type': ('exact',)
        }


class DetailSectionResource(BaseModelResource):

    images = fields.ToManyField(DetailSectionImageResource, 'images', full=True)

    class Meta(BaseModelResource.Meta):
        resource_name = 'detail_sections'
        collection_name = resource_name
        allowed_methods = []
        queryset = DetailSection.objects.active()
        fields = ('label',)


class DetailResource(DetailMixin, BaseModelResource):

    title_image = fields.ToOneField(DetailImageResource, 'title_image', full=True)
    sections = fields.ToManyField(DetailSectionResource, 'sections', full=True)

    class Meta(BaseModelResource.Meta):
        resource_name = 'details'
        collection_name = resource_name
        allowed_methods = ['get']
        queryset = Detail.objects.active().select_related('image')
        fields = ('name', 'caption', 'facts', 'video_url', 'type')
        detail_fields = ('caption', 'facts', 'video_url')
        filtering = {
            'type': ('exact',)
        }

    def get_list(self, request, **kwargs):
        raise ImmediateHttpResponse(http.HttpNotFound('Not found.'))


class EmbeddedDetailResource(DetailResource):
    """
    This resource is not registered in urls.py. Needed only for SubcategoryResource.
    """

    title_image = fields.ToOneField(SubcategoryImageResource, 'title_image', full=True)

    class Meta(DetailResource.Meta):
        fields = ('id', 'name',)
        queryset = Detail.objects.active().only('name').select_related('image')


class SubcategoryResource(BaseModelResource):

    details = fields.ToManyField(EmbeddedDetailResource, 'details', full=True, null=True, blank=True)

    class Meta(BaseModelResource.Meta):
        resource_name = 'subcategories'
        collection_name = resource_name
        allowed_methods = ['get']
        queryset = Subcategory.objects.active().prefetch_related('details')
        fields = ('name', 'caption', 'type')
        filtering = {
            'type': ('exact',),
        }

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(SubcategoryResource, self).build_filters(filters)

        if 'category' in filters:
            orm_filters['category_id'] = filters['category']

        return orm_filters
