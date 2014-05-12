# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'materials.views.material_list', name='material_list'),
    url(r'^(?P<category_id>\d+)/subcategories/$', 'materials.views.material_subcategory',
        name='material_subcategories'),
    url(r'^detail/(?P<material_id>\d+)/$', 'materials.views.material_detail', name='material_detail')
)