
from rest_framework import serializers
from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')  #this is for bydefault set username, when adding data does'nt shows poster option,but after submitting automatically user name give 
    poster_id = serializers.ReadOnlyField(source='poster.id') # this will show user id 
    votes = serializers.SerializerMethodField()     # this is for creating vote option

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster',
                  'poster_id', 'created', 'votes']

    def get_votes(self, post):        # getting total votes per single entry
        return Vote.objects.filter(post=post).count()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']
