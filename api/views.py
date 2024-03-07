from rest_framework import generics
from main.models import Manga
from .serializers import AnimeSerializer

class AnimeListCreate(generics.ListCreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = AnimeSerializer

class AnimeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = AnimeSerializer
    lookup_field = 'id'