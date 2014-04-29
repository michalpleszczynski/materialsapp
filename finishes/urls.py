# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'core.views.subcategory',
        {'ajax_function': 'Dajaxice.finishes.get_subcategories(Dajax.process)'}, name='finish_list'),
    url(r'^detail/(?P<finish_id>\w+)/$', 'finishes.views.finish_detail',
        {'ajax_function': "Dajaxice.finishes.get_detail(Dajax.process, {'detail_id': {0} })"}, name='finish_detail')
)