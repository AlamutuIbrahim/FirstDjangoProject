from rest_framework import serializers
from . models import *

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Artiste
        fields = ('first_name',)


class SongSerializer(serializers.ModelSerializer):
    class Meta():
        model = Song
        fields = ('title', )

class LyricSerializer(serializers.ModelSerializer):
    class Meta():
        model = Lyric
        fields = ('song', )