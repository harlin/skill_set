# from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from skill_tracker.skill_set.models import Skill, SubSkill, SubSkillKnowledge
from django.forms import ModelForm


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

@login_required
def my_skills(request):
    skill_list = Skill.objects.all()
    return render_to_response('skill_set/my_skills.html', {'skill_list': skill_list})

class KnowledgeForm(ModelForm):
    class Meta:
        model = SubSkillKnowledge

@login_required
def my_skill_input(request, skill_id):
    # TODO: add some real stuff here
    s = get_object_or_404(Skill, pk=skill_id)
    if request.method == 'POST': # If the form has been submitted...
        form = KnowledgeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/my_skills/') # Redirect after POST
    else:
        form = KnowledgeForm() # An unbound form
    return render_to_response('skill_set/my_skill_input.html', {'skill': s, 'form': form}, \
        context_instance=RequestContext(request))
