# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .models import FinishSubcategory

subcategory_info = {
    'subcategories': FinishSubcategory.objects.active(),
    'detail_url': 'finish_detail',
    'active_link': '#finishes_link',
    'base_template': 'base.html'
}

detail_info = {
    'active_link': '#finishes_link',
    'base_template': 'base.html'
}

urlpatterns = patterns('',
    url(r'^$', 'core.views.subcategory', subcategory_info, name='finish_list'),
    url(r'^detail/(?P<detail_id>\w+)/$', 'core.views.detail', detail_info, name='finish_detail')
)