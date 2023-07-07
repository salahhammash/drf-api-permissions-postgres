from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Game(models.Model):
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()    
    
    def __str__ (self):
        # return self.name
        return self.title