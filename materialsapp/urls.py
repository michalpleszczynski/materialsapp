# coding: utf-8
from __future__ import unicode_literals

from tastypie.api import Api
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from core.api import CategoryResource, SubcategoryResource, DetailResource, ImageResource

admin.autodiscover()
dajaxice_autodiscover()

api_v1 = Api(api_name='v1')
api_v1.register(CategoryResource())
api_v1.register(SubcategoryResource())
api_v1.register(DetailResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^api/', include(api_v1.urls)),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^api/v1/search/', 'core.views.search', name='search'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )