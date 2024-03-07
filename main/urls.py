from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('anime/<slug:slug>', views.manga_detail, name="manga_detail"),
    path('genre/<slug:genre_slug>', views.mangas_by_genre, name="mangas_by_genre"),
]