from django.contrib import admin
from .models import Manga, Genre, Rating, Volume, Chapter

admin.site.register(Manga)
admin.site.register(Genre)
admin.site.register(Rating) 
admin.site.register(Volume)
admin.site.register(Chapter)