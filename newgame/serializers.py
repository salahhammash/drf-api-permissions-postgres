from rest_framework import serializers
from .models import Game,Post

class GameSerializer(serializers.ModelSerializer):
    class Meta :
        model = Game
        fields =("id","owner","name","desc","created_at","updated_at")
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = ('title', 'desc')    