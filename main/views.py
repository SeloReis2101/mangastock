from django.shortcuts import render, redirect, get_object_or_404
from .models import Manga, Genre, Rating, Volume, Chapter
from comments.models import Comment, CommentReply
from .utils import time_ago_in_words

import random

def home(request):
    all_mangas = Manga.objects.all().order_by('-id')
    random_mangas = random.sample(list(all_mangas), 5)
    # random_mangas = []
    params = {'all_mangas': all_mangas, 'random_mangas': random_mangas}
    return render(request, 'main/index.html', params)

def manga_detail(request, slug):
    manga = get_object_or_404(Manga, slug=slug)
    manga.views_count += 1
    manga.save()
    # chapters
    chapters = Chapter.objects.filter(volume__manga=manga)
    # comments
    comments = Comment.objects.filter(content_type__model='manga', object_id=manga.id)
    for comment in comments:
        comment.time_ago = time_ago_in_words(comment.created_at)
        comment.save()
    params = {'manga': manga, 'chapters': chapters, 'comments': comments}
    return render(request, 'main/manga-detail.html', params)

def mangas_by_genre(request, genre_slug):
    genre = get_object_or_404(Genre, slug=genre_slug)
    mangas = Manga.objects.filter(genres=genre)
    params = {'mangas': mangas, 'title': genre.slug}
    return render(request, 'main/manga-page.html', params)