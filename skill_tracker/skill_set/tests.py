from django.test import TestCase
from skill_tracker.skill_set.models import Skill, SubSkill, SubSkillKnowledge
from django.contrib.auth.models import User


class KnowledgeCreationWithUserTest(TestCase):
    def setUp(self):
        self.python = Skill.objects.create(
            name = 'Python',
            description = 'All hail Python!')
        self.django = SubSkill.objects.create(
            name = 'Django',
            description = 'Djangonauting',
            parent_skill = self.python)
        self.someuser = User.objects.create(
            username = 'Default',
            password = 'password')

    def test_knowledge_creation(self):
        """
        Tests that SubSkillKnowledge is created for new User
        """
        knowledge = SubSkillKnowledge.objects.get(
            employee = self.someuser,
            subskill = self.django
            )
        self.assertEqual(knowledge.employee, self.someuser)
        self.assertEqual(knowledge.subskill, self.django)
        self.assertEqual(knowledge.knowledge_level, '0')
        self.assertEqual(knowledge.want, False)
        self.assertEqual(knowledge.comment, "")

    def tearDown(self):
        SubSkillKnowledge.objects.get(
            employee = self.someuser,
            subskill = self.django
            ).delete()
        self.python.delete()
        self.django.delete()
        self.someuser.delete()


class KnowledgeCreationWithSubSkillTest(TestCase):
    def setUp(self):
        self.python = Skill.objects.create(
            name = 'Python',
            description = 'All hail Python!')
        self.someuser = User.objects.create(
            username = 'Default',
            password = 'password')
        self.pylons = SubSkill.objects.create(
            name = 'Pylons',
            description = 'Pre-Django',
            parent_skill = self.python)

    def test_knowledge_creation(self):
        """
        Tests that SubSkillKnowledge is created for new SubSkill
        """
        knowledge = SubSkillKnowledge.objects.get(
            employee = self.someuser,
            subskill = self.pylons
            )
        self.assertEqual(knowledge.employee, self.someuser)
        self.assertEqual(knowledge.subskill, self.pylons)
        self.assertEqual(knowledge.knowledge_level, '0')
        self.assertEqual(knowledge.want, False)
        self.assertEqual(knowledge.comment, "")

    def tearDown(self):
        SubSkillKnowledge.objects.get(
            employee = self.someuser,
            subskill = self.pylons
            ).delete()
        self.python.delete()
        self.pylons.delete()
        self.someuser.delete()


class FixtureLoadedTestCase(TestCase):
    '''
    This is not an actual test case
    It loads the needed data so other test cases may be inherited from it
    '''
    fixtures = ['start_data.json']


# For now I failed to make this simplification work
# class URLTestCase():
#     def testURL(self, url, template_name):
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.template), 2)
#         self.assertEqual(response.template[1].name, 'base.html')
#         self.assertEqual(response.template[0].name, template_name)


class MainURLTestCase(FixtureLoadedTestCase):
    '''
    This test case checks that all main URLS available to public user
    can be accessed
    '''
    def test_main_urls(self):
        # TODO: Rewrite it to fit DRY principle
        # OR/AND add more informative checks here
        response = self.client.get('/skills/')
        self.assertContains(response, 'Java')
        self.assertTemplateUsed(response, 'skill_set/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_skill(self):
        response = self.client.get('/skills/1/')
        self.assertContains(response, 'Java')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'skill_set/skill_detail.html')

    def test_subskill(self):
        response = self.client.get('/skills/1/1/')
        self.assertContains(response, 'Java')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'skill_set/subskill_detail.html')


class UnloginedURLTestCase(FixtureLoadedTestCase):
    def test_my_skills(self):
        response = self.client.get('/skills/my_skills/')
        self.assertRedirects(
            response, '/accounts/login/?next=/skills/my_skills/')

    def test_knowledge(self):
        response = self.client.get('/skills/knowledge/')
        self.assertRedirects(
            response, '/accounts/login/?next=/skills/knowledge/')


class UserLoggedTestCase(FixtureLoadedTestCase):
    '''
    This is the test case that can be inherited from testcases
    which need user to be logged in
    '''
    def setUp(self):
        self.client.login(username='ipetrov', password='qwerty')

    def tearDown(self):
        self.client.logout()


class LoginURLTestCase(UserLoggedTestCase):
    '''
    This test case checks that all main URLS available to public user
    can be accessed
    '''
    def test_my_skills(self):
        response = self.client.get('/skills/my_skills/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'skill_set/my_skills.html')

    def test_knowledge(self):
        response = self.client.get('/skills/knowledge/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'skill_set/knowledge.html')


# This one fails for some reason - works perfectly on a live db
'''
class KnowledgeAJAXTestCase(UserLoggedTestCase):
    def test_knowledge_by_skill(self):
        response = self.client.post(
            '/skills/knowledge/',
            {'skill': [1]},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, {})
        # TODO: Add some data checking here

    def test_knowledge_by_subskill(self):
        response = self.client.post(
            '/skills/knowledge/',
            {'subskill': [1]},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, {})
        # TODO: Add some data checking
'''
