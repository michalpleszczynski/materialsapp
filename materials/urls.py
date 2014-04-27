# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'materials.views.material_list',
        {'ajax_function': 'Dajaxice.materials.get_materials(Dajax.process)'}, name='material_list'),
    url(r'^(?P<material_id>\w+)/subcategories/$', 'materials.views.material_subcategories',
        {'ajax_function': "Dajaxice.materials.get_subcategories(Dajax.process, {'material_id': {0} })"},
        name='material_subcategories')
)