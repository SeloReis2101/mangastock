from django.urls import path
from .import views

urlpatterns = [
    path('library/', views.library, name="library"),
    path('view_library/', views.view_library, name="view_library"),
    path('history/', views.history, name="history"),
]