from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Game


# Create your tests here.

class GameTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_thing = Game.objects.create(name='flower', owner=testuser1, desc="test desc ...")
        test_thing.save()

    def test_games_model(self):
        gameing = Game.objects.get(id=1)
        actual_owner= str(gameing.owner)
        actual_name = str(gameing.name)
        actual_desc = str(gameing.desc)
        self.assertEqual(actual_owner,"testuser1")
        self.assertEqual(actual_name,"flower")
        self.assertEqual(actual_desc,"test desc ...")
    
    def tes_postgress(self):
        pass 
            
        
        