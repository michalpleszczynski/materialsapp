# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'core.views.subcategory',
        {'ajax_function': 'Dajaxice.joins.get_subcategories(Dajax.process)'}, name='join_list'),
    url(r'^detail/(?P<join_id>\w+)/$', 'joins.views.join_detail',
        {'ajax_function': "Dajaxice.joins.get_detail(Dajax.process, {'detail_id': {0} })"}, name='join_detail')
)