from django.conf.urls.defaults import *

urlpatterns = patterns('skill_tracker.skill_set.views',
    (r'^$', 'skill_index'),
    (r'^(?P<skill_id>\d+)/$', 'skill_detail'),
    (r'^(?P<skill_id>\d+)/(?P<subskill_id>\d+)/$', 'subskill_detail'),
    (r'^my_skills/$', 'my_skills'),
    (r'^my_skills/(?P<skill_id>\d+)/$', 'my_skill_input'),

)
