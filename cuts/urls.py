# coding: utf-8
from django.conf.urls import patterns, url

from .models import CutSubcategory

subcategory_info = {
    'subcategories': CutSubcategory.objects.active(),
    'detail_url': 'cut_detail',
    'active_link': '#cuts_link',
    'base_template': 'base.html'
}

detail_info = {
    'active_link': '#cuts_link',
    'base_template': 'base.html'
}

urlpatterns = patterns('',
    url(r'^$', 'core.views.subcategory', subcategory_info, name='cut_list'),
    url(r'^detail/(?P<detail_id>\w+)/$', 'core.views.detail', detail_info, name='cut_detail')
)