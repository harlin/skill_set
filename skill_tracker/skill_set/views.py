from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from skill_tracker.skill_set.models import Skill, SubSkill

def skill_index(request):
    skill_list = Skill.objects.all()
    return render_to_response('skill_set/index.html', {'skill_list': skill_list})

def skill_detail(request, skill_id):
    s = get_object_or_404(Skill, pk=skill_id)
    return render_to_response('skill_set/skill_detail.html', {'skill': s})

def subskill_detail(request, skill_id, subskill_id):
    s = get_object_or_404(Skill, pk=skill_id)
    sub = get_object_or_404(SubSkill, pk=subskill_id)
    return render_to_response('skill_set/subskill_detail.html', {'skill': s, 'subskill': sub})

# @login_required(redirect_field_name='redirect_to')
@login_required
def my_skills(request):
    # TODO: add some real stuff here
    return render_to_response('skill_set/my_skills.html')
