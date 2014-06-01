# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .models import FormSubcategory

subcategory_info = {
    'subcategories': FormSubcategory.objects.active(),
    'detail_url': 'form_detail',
    'active_link': '#forms_link',
    'base_template': 'base.html'
}

detail_info = {
    'active_link': '#forms_link',
    'base_template': 'base.html'
}

urlpatterns = patterns('',
    url(r'^$', 'core.views.subcategory', subcategory_info, name='form_list'),
    url(r'^detail/(?P<detail_id>\w+)/$', 'core.views.detail', detail_info, name='form_detail')
)