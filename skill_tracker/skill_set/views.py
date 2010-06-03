from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from skill_tracker.skill_set.models import Skill, SubSkill, SubSkillKnowledge
from django.forms import ModelForm
from django.forms.models import modelformset_factory




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
    # TODO: fix this
    s = get_object_or_404(Skill, pk=skill_id)
    for sub in s.subskill_set.all():
        SubSkillKnowledge.objects.get_or_create(
            employee=request.user, subskill=sub)
    KnowledgeFormSet = modelformset_factory(SubSkillKnowledge, \
        max_num=s.subskill_set.count())
    if request.method == 'POST': # If the form has been submitted...
        from settings import DEBUG
        if DEBUG:
            postfile = open('postfile.txt', 'w')
            print >> postfile, request.POST
            postfile.close()
        data = dict(request.POST.items())
        data['form-TOTAL_FORMS'] = s.subskill_set.count()
        data['form-INITIAL_FORMS'] = s.subskill_set.count()
        data['form-MAX_NUM_FORMS'] = s.subskill_set.count()
        form_list = KnowledgeFormSet(data)
        if form_list.is_valid():
            form_list.save()
            return HttpResponseRedirect('/skills/my_skills/') # Redirect after POST
    else:
        form_list = KnowledgeFormSet(queryset=SubSkillKnowledge.objects.filter(
            employee=request.user))
    return render_to_response('skill_set/my_skill_input.html', {'skill': s, 'form_list': form_list}, \
        context_instance=RequestContext(request))
