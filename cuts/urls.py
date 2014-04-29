# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'core.views.subcategory',
        {'ajax_function': 'Dajaxice.cuts.get_subcategories(Dajax.process)'}, name='cut_list'),
    url(r'^detail/(?P<cut_id>\w+)/$', 'cuts.views.cut_detail',
        {'ajax_function': "Dajaxice.cuts.get_detail(Dajax.process, {'detail_id': {0} })"}, name='cut_detail')
)