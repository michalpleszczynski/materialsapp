# coding: utf-8
from __future__ import unicode_literals

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
    url(r'^join/', include('joins.urls')),
    url(r'^cut/', include('cuts.urls')),
    url(r'^finish/', include('finishes.urls')),
    url(r'^form/', include('forms.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )