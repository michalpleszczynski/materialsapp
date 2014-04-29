# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'core.views.subcategory',
        {'ajax_function': 'Dajaxice.forms.get_subcategories(Dajax.process)'}, name='form_list'),
    url(r'^detail/(?P<form_id>\w+)/$', 'forms.views.form_detail',
        {'ajax_function': "Dajaxice.forms.get_detail(Dajax.process, {'detail_id': {0} })"}, name='form_detail')
)