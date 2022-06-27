#importing library.
from rest_framework import serializers
from .models import Post, Vote

#Creating a class called PostSerializer.
class PostSerializer(serializers.ModelSerializer):
    #Assinging poster a value.
    poster = serializers.ReadOnlyField(source='poster.username')
    #Creating a poster_id.
    poster_id = serializers.ReadOnlyField(source='poster.id')
    #Creating a class named Meta.
    class Meta:
        #Creating a model variable pointing to post.
        model = Post
        #Creating an array of strings.
        fields = ['id', 'title', 'url', 'poster', 'poster_id', 'created']
#Creating a new class for voting called VoteSerializer.
class VoteSerializer(serializers.ModelSerializer):
    #Creating a child class.
    class Meta:
        #Assigned a variable to a Vote object.
        model = Vote
        #Creating a list of fields.
        fields = ['id']
    