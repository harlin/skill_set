from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^skills/', include('skill_tracker.skill_set.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # (r'^accounts/profile/$', 'django.contrib.auth.views.profile'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
)
