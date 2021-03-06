from django.test import TestCase
from django.contrib.auth.models import Group
from workflow.models import Profile, Assignment
from mainsite.models import Issue, Section, Article

class WorkflowModels(TestCase):
    def test_initial_data(self):
        kent = Group.objects.all()[3].user_set.all()[0]
        self.assertEqual("kshikama", kent.username)
        print("password for kent: " + kent.password)

        ziqi = Group.objects.all()[3].user_set.all()[1]
        self.assertEqual("zxiong", ziqi.username)
        print("password for ziqi: " + ziqi.password)

        latina = Group.objects.all()[3].user_set.all()[2]
        self.assertEqual("vlatina", latina.username)
        print("password for latina: " + latina.password)

        self.print_profiles()
        self.print_sections()
        self.print_articles()
        self.print_assignments()

    def test_kent_profile(self):
        kent = Group.objects.all()[3].user_set.all()[0]
        kent.first_name = "Kent"
        kent.last_name = "Shikama"

        profile_kent = Profile(user=kent, position='photographer')
        self.assertEqual("Kent Shikama", profile_kent.user.get_full_name())

    def print_assignments(self):
        assignments = Assignment.objects.all()
        for assignment in assignments:
            print("assignment title: " + assignment.title)
            print("assignment content: " + assignment.content)
            print("assignment sender: " + assignment.sender.user.username)
            print("assignment recipient: " + assignment.receiver.user.username)

    def print_articles(self):
        articles = Article.objects.all()
        for article in articles:
            print("article title: " + article.title)
            if article.authors.all()[0].user:
                print("article author: " + article.authors.all()[0].user.username)
            print("article content: " + article.content)

    def print_sections(self):
        sections = Section.objects.all()
        for section in sections:
            print("section name: " + section.name)

    def print_profiles(self):
        profiles = Profile.objects.all()
        for profile in profiles:
            if profile.user:
                print("profile user: " + profile.user.username)
                print("profile position: " + profile.position)