from django.contrib import admin
from skill_tracker.skill_set.models import Skill, SubSkill

class SubSkillInline(admin.StackedInline):
    model = SubSkill
    extra = 3

class SkillAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Information', {'fields': ['name', 'description']}),
        # ('Links',               {'fields': ['homepage', 'wiki_en_link'], 'classes': ['collapse']}),
    ]
    inlines = [SubSkillInline]


admin.site.register(Skill, SkillAdmin)
