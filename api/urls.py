from django.urls import path
from .views import AnimeListCreate, AnimeRetrieveUpdateDestroy

urlpatterns = [
    path('anime/', AnimeListCreate.as_view(), name='anime-list'),
    path('anime/<int:id>/', AnimeRetrieveUpdateDestroy.as_view(), name='anime-detail'),
]