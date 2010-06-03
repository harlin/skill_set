from skill_tracker.skill_set.models import Skill, SubSkill, SubSkillKnowledge
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.forms.models import modelformset_factory, inlineformset_factory


def skill_index(request):
    skill_list = Skill.objects.all()
    return render_to_response('skill_set/index.html', \
        {'skill_list': skill_list})

def skill_detail(request, skill_id):
    s = get_object_or_404(Skill, pk=skill_id)
    return render_to_response('skill_set/skill_detail.html', {'skill': s})

def subskill_detail(request, skill_id, subskill_id):
    s = get_object_or_404(Skill, pk=skill_id)
    sub = get_object_or_404(SubSkill, pk=subskill_id)
    return render_to_response('skill_set/subskill_detail.html', \
        {'skill': s, 'subskill': sub})

@login_required
def my_skills(request):
    skill_list = Skill.objects.all()
    return render_to_response('skill_set/my_skills.html', \
        {'skill_list': skill_list})


# class KnowledgeForm(ModelForm):
#     class Meta:
#         model = SubSkillKnowledge

@login_required
def my_skill_input(request, skill_id):
    s = get_object_or_404(Skill, pk=skill_id)
    skill_list = Skill.objects.all()

    # Create objects if they don't exist yet
    # TODO: This looks like a bit hardcode AND it violates MVC
    #       but for now i don't know how (or where) to do it better
    for sub in s.subskill_set.all():
        SubSkillKnowledge.objects.get_or_create(
            employee=request.user, subskill=sub)

    # TODO: I should add a custom form argument here OR work on template
    KnowledgeFormSet = inlineformset_factory(User, SubSkillKnowledge, \
        extra=0, can_delete=False, fields=(
            'subskill', 'knowledge_level', 'want', 'comment'))
    if request.method == 'POST':
        formset = KnowledgeFormSet(request.POST, instance=request.user)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/skills/my_skills/')
    else:
        formset = KnowledgeFormSet(instance=request.user)
    return render_to_response('skill_set/my_skill_input.html', \
        {'skill': s, 'formset': formset, 'skill_list': skill_list}, \
            context_instance=RequestContext(request))
