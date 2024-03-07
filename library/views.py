from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from authentication.models import User
from .models import LibraryList, History

import random

@login_required
def library(request):
    libraries = LibraryList.objects.filter(user=request.user)
    all_mangas = []
    for library in libraries:
        for manga in library.mangas.all():
            all_mangas.append(manga)
    random_manga = random.sample(list(all_mangas), 1)
    params = {'libraries': libraries, 'random_manga': random_manga}
    return render(request, 'library/library.html', params)

@login_required
def history(request):
    histories = History.objects.filter(user=request.user)
    latest_history = histories.latest('lastread_at')
    previous_histories = histories.exclude(id=latest_history.id)
    params = {'histories': previous_histories, 'last_history': latest_history}
    return render(request, 'library/history.html', params)


# def view_library(request, library_id):
#     library = get_object_or_404(LibraryList, pk=library_id)
#     # if request.method == 'POST':

#     mangas = []
#     for manga in library.mangas.all():
#         mangas.append({
#             'title': manga.title,
#             'cover_image': manga.cover_image.url,
#             'slug': manga.slug,
#         })
        
#     params = {
#         'title': library.title,
#         'mangas': mangas,
#     }
#     return JsonResponse(params)

def view_library(request):
    if request.method == 'GET':
        library_id = request.GET["library_id"]
        library = get_object_or_404(LibraryList, pk=library_id)

    mangas = []
    for manga in library.mangas.all():
        mangas.append({
            'title': manga.title,
            'cover_image': manga.cover_image.url,
            'slug': manga.slug,
        })
        
    params = {
        'title': library.title,
        'mangas': mangas,
    }
    return JsonResponse(params)

# def add_library(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         manga_ids = request.POST["manga_ids"]
        
#     params = {'success': 'Ok'}
#     return JsonResponse(params)