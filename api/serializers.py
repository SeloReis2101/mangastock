from rest_framework import serializers
from main.models import Manga

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ('id', 'title', 'description', 'cover_image')