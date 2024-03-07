from django.db import models
from main.models import Manga, Chapter
from authentication.models import User

class LibraryList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    mangas = models.ManyToManyField(Manga)

    def __str__(self):
        return self.title

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    last_page = models.IntegerField(default=1)
    lastread_at = models.DateField(auto_now_add=True)