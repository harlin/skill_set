from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=200)
    # logo = models.ImageField(upload_to='skill_set/img/')
    # TODO: learn more about images later. looks like PIL is needed here
    description = models.TextField()
    # wiki_en_link = models.URLField(verify_exists=True, max_length=200, blank=True)
    # homepage = models.URLField(verify_exists=True, max_length=200, blank=True)
    def __unicode__(self):
        return self.name

class SubSkill(models.Model):
    parent_skill = models.ForeignKey(Skill)
    name = models.CharField(max_length=200)
    # logo = models.ImageField(upload_to='skill_set/img/')
    # TODO: learn more about images later. looks like PIL is needed here
    description = models.TextField()
    wiki_en_link = models.URLField(verify_exists=True, max_length=200, blank=True)
    homepage = models.URLField(verify_exists=True, max_length=200, blank=True)
    def __unicode__(self):
        return self.name

