from dajaxice.core import dajaxice_autodiscover, dajaxice_config

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    url(r'^$', 'core.views.home', name='home'),
    url(r'^view_detail/(?P<id>\w+)$', 'core.views.detail', name='detail'),
    url(r'^materials/', include('materials.urls')),
    url(r'^cut/$', 'core.views.subcategory',
        {'ajax_function': 'Dajaxice.cuts.get_subcategories(Dajax.process)'}, name='cut_list'),
    url(r'^finish/$', 'core.views.subcategory',
        {'ajax_function': 'Dajaxice.finishes.get_subcategories(Dajax.process)'}, name='finish_list'),
    url(r'^form/$', 'core.views.subcategory',
        {'ajax_function': 'Dajaxice.forms.get_subcategories(Dajax.process)'}, name='form_list'),
    url(r'^join/$', 'core.views.subcategory',
        {'ajax_function': 'Dajaxice.joins.get_subcategories(Dajax.process)'}, name='join_list'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )