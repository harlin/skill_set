from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=200)
    # logo = models.ImageField(upload_to='skill_set/img/')
    # TODO: learn more about images later. looks like PIL is needed here
    description = models.TextField()
    wiki_en_link = models.URLField(
        verify_exists=True, max_length=200, blank=True)
    homepage = models.URLField(verify_exists=True, max_length=200, blank=True)

    def __unicode__(self):
        return self.name


class SubSkill(models.Model):
    parent_skill = models.ForeignKey(Skill)
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='img', blank=True)
    # TODO: learn more about images later. looks like PIL is needed here
    description = models.TextField()
    wiki_en_link = models.URLField(
        verify_exists=True, max_length=200, blank=True)
    homepage = models.URLField(verify_exists=True, max_length=200, blank=True)

    def __unicode__(self):
        return self.name


from django.contrib.auth.models import User

KNOWLEDGE_CHOICES = (
    ('0', "Don't know at all"),
    ('1', "Tried a few things"),
    ('2', "Had a project"),
    ('3', "Mastered"),
)


class SubSkillKnowledge(models.Model):
    employee = models.ForeignKey(User)
    subskill = models.ForeignKey(SubSkill)
    knowledge_level = models.CharField(max_length=1, \
        choices=KNOWLEDGE_CHOICES, default='0')
    want = models.BooleanField(default=False)
    comment = models.TextField(blank=True)

from django.db.models.signals import post_save


def create_knowledge_for_user(sender, instance, created, **kwargs):
    if created:
        for sub in SubSkill.objects.all():
            SubSkillKnowledge.objects.create(employee=instance, subskill=sub)

post_save.connect(create_knowledge_for_user, sender=User)


def create_knowledge_for_subskill(sender, instance, created, **kwargs):
    if created:
        for user in User.objects.all():
        # TODO: change this to work only on employee user group
            SubSkillKnowledge.objects.create(employee=user, subskill=instance)

post_save.connect(create_knowledge_for_subskill, sender=SubSkill)
