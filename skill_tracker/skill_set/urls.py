from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('skill_tracker.skill_set.views',
    # Example:
    (r'^$', 'skill_index'),
    (r'^(?P<skill_id>\d+)/$', 'skill_detail'),
    (r'^(?P<skill_id>\d+)/(?P<subskill_id>\d+)/$', 'subskill_detail'),
    (r'^my_skills/$', 'my_skills'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
