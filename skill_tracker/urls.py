from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    (r'^skills/', include('skill_tracker.skill_set.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # (r'^accounts/profile/$', 'django.contrib.auth.views.profile'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
)

#if settings.DEBUG:
urlpatterns += patterns('',
    url(r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    # url(r'^admin-media/(.*)$', 'django.views.static.serve',
    #     {'document_root': join(dirname(admin.__file__), 'media')}),
    )
