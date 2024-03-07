import zipfile
import os
from django.core.files import File
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from authentication.models import User
from comments.models import Comment

class Manga(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Author")
    description = RichTextField()
    short_desc = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='anime_covers')
    slug = models.SlugField(unique=True, blank=True)
    genres = models.ManyToManyField('Genre')
    connected_mangas = models.ManyToManyField('self', blank=True)
    views_count = models.IntegerField(default=0) # for popular filtering

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def comments(self):
        return Comment.objects.filter(content_type__model='manga', object_id=self.id)

    def __str__(self):
            return self.title

class Volume(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='volume_covers/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.manga.title} - Volume {self.title}"

class Chapter(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    chapter_number = models.IntegerField()
    cbz_file = models.FileField(upload_to="chapters")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        self.extract_and_save_pages()
    
    def extract_and_save_pages(self):
        cbz_path = self.cbz_file.path
        extract_path = f'media/manga_pages/{self.slug}/'

        with zipfile.ZipFile(cbz_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        for page_number, file_name in enumerate(sorted(os.listdir(extract_path))):
            page_path = os.path.join(extract_path, file_name)
            with open(page_path, 'rb') as f:
                manga_page = MangaPage(chapter=self, page_number=page_number + 1)
                manga_page.image.save(file_name, File(f))
                manga_page.save()

    def comments(self):
        return Comment.objects.filter(content_type__model='chapter', object_id=self.id)

    def __str__(self):
        return f"{self.volume.manga.title} - Volume {self.volume.title} - Chapter {self.chapter_number}: {self.title}"

class MangaPage(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)
    page_number = models.IntegerField()
    image = models.ImageField(upload_to='manga_pages/')

    def __str__(self):
        return f"Page {self.page_number} of {self.chapter}"

class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    rating = models.IntegerField()
