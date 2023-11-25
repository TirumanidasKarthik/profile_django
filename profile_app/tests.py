from django.test import TestCase
from django.conf import settings

from .views import bio 

# Create your tests here.

class Tests(TestCase):
    def setup(self):
        pass

    def test_file_exist(self):
        try:
            with open( settings.MEDIA_ROOT + '/profile_app/bio.txt', 'r') as f:
                pass
            assert True
        except:
            assert False

    def test_bio(self):
        with open( settings.MEDIA_ROOT + '/profile_app/bio.txt', 'r') as f:
            data = f.read()
            assert data != None
        
