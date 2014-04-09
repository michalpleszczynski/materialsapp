from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),

    url(r'^material_list/$', 'materials.views.material_list', name='material_list'),
    url(r'^view_material/(?P<id>\w+)$', 'materials.views.material_detail', name='material_detail'),

    url(r'^join_list/$', 'joins.views.join_list', name='join_list'),
    url(r'^form_list/$', 'forms.views.form_list', name='form_list'),
    url(r'^finish_list/$', 'finishes.views.finish_list', name='finish_list'),
    url(r'^cut_list/$', 'cuts.views.cut_list', name='cut_list'),

    url(r'^admin/', include(admin.site.urls)),
)
