from django.test import TestCase
from django.conf import settings


# Create your tests here.

class Tests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.files = ['achievement.json', 'bio.txt', 'certification.json', 'education.json',
                 'experience.json', 'skills.json']

    def test_files_exist(self):
        for file in self.files:
            try:
                with open( settings.MEDIA_ROOT + '/profile_app/' + file, 'r') as f:
                    pass
                assert True
            except:
                assert False

    
        
