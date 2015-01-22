# coding: utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    'example.views',

    url(r'^$', 'index', name='index'),
    url(r'^post/(?P<post_id>\d+)/$', 'get_post', name='get_post'),

    url(r'^stats/', include('statsy.urls', namespace='statsy')),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
