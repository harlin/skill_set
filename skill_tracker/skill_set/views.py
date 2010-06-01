from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from skill_tracker.skill_set.models import Skill, SubSkill
from django import forms

class SomeForm(forms.Form):
    somefield = forms.CharField(max_length=100)

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
    if request.method == 'POST': # If the form has been submitted...
        form = SomeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            # return HttpResponseRedirect('/thanks/') # Redirect after POST
            pass
    else:
        form = SomeForm() # An unbound form

    return render_to_response('skill_set/my_skills.html', {
        'form': form,
    }, context_instance=RequestContext(request))
