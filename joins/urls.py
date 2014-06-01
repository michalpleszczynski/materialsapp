# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .models import JoinSubcategory

subcategory_info = {
    'subcategories': JoinSubcategory.objects.active(),
    'detail_url': 'join_detail',
    'active_link': '#joins_link',
    'base_template': 'base.html'
}

detail_info = {
    'active_link': '#joins_link',
    'base_template': 'base.html'
}

urlpatterns = patterns('',
    url(r'^$', 'core.views.subcategory', subcategory_info, name='join_list'),
    url(r'^detail/(?P<detail_id>\w+)/$', 'core.views.detail', detail_info, name='join_detail')
)