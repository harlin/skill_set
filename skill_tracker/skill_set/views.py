from skill_tracker.skill_set.models import Skill, SubSkill, SubSkillKnowledge
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory, inlineformset_factory
from django.utils import simplejson

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
    # subskill_list = SubSkill.objects.all()
    # levels = [ {'id': ch[0], 'name': ch[1]} for ch in KNOWLEDGE_CHOICES ]

    KnowledgeFormSet = inlineformset_factory(User, SubSkillKnowledge, \
        extra=0, can_delete=False, fields=(
            'knowledge_level', 'want', 'comment'))

    if request.method == 'POST':
        formset = KnowledgeFormSet(request.POST, instance=request.user)
        if formset.is_valid():
            formset.save()
            if not request.is_ajax():
                return HttpResponseRedirect('/skills/my_skills/')
    else:
        formset = KnowledgeFormSet(instance=request.user)
    return render_to_response('skill_set/my_skills.html', \
        {'formset': formset, 'skill_list': skill_list}, \
            context_instance=RequestContext(request))



@login_required
def knowledge(request):
    skill_list = Skill.objects.all()
    subskill_list = SubSkill.objects.all()
    if request.method == 'POST':
        if request.is_ajax():
            sub_list = []
            user_list = []
            if request.POST.has_key('subskill'):
                s_name = request.POST['subskill']
                sub_list = [
                    get_object_or_404(
                        SubSkill, pk=s_name[0]
                        )
                    ]
            elif request.POST.has_key('skill'):
                s_name = request.POST['skill']
                s = get_object_or_404(
                        Skill, pk=s_name[0]
                        )
                sub_list = s.subskill_set.all()
            # if not sub_list:
            #     return render_to_response('skill_set/knowledge.html', \
            #         {'text': 'Please select skill or subskill'}, \
            #             context_instance=RequestContext(request))
            user_list = []
            for sub in sub_list:
                # This probably should be refactored using list comprehension
                for k in sub.subskillknowledge_set.all():
                    if k.knowledge_level != '0' or k.want:
                        user_list.append(k.employee)
            user_list = list(set(user_list))
            data = {}
            data['skill_count'] = len(sub_list)
            data['user_count'] = len(user_list)
            data['skills'] = [{'id': sub.id, 'name': sub.name} for sub in sub_list]
            data['users'] = [{
                'id': user.id, 
                'name': user.username,
                'knowledges': [{
                    'id': sub.id, 
                    'level': SubSkillKnowledge.objects.get(
                        employee=user, subskill=sub
                        ).knowledge_level,
                    'want': SubSkillKnowledge.objects.get(
                        employee=user, subskill=sub
                        ).want
                    } for sub in sub_list]
                } for user in user_list]
            return HttpResponse(simplejson.dumps({'data': data}), \
                mimetype="application/json")
        else:
            return render_to_response('skill_set/knowledge.html', \
                {
                    'skill_list': skill_list,
                    'subskill_list': subskill_list,
                    'text': 'No ajax'}, \
                    context_instance=RequestContext(request))
    else:
        return render_to_response('skill_set/knowledge.html', \
            {
                'skill_list': skill_list,
                'subskill_list': subskill_list,
                'text': 'Please select skill or subskill'}, \
                context_instance=RequestContext(request))

# @login_required
# def knowledge_of_skill(request, skill_id):
#     s = get_object_or_404(Skill, pk=skill_id)
#     return render_to_response('skill_set/knowledge_of_skill.html', {'skill': s})

# @login_required
# def knowledge_of_subskill(request, skill_id, subskill_id):
#     s = get_object_or_404(Skill, pk=skill_id)
#     sub = get_object_or_404(SubSkill, pk=subskill_id)
#     return render_to_response('skill_set/knowledge_of_subskill.html', \
#         {'skill': s, 'subskill': sub})
