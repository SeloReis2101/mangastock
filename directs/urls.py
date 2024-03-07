from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:chat_id>/', views.chat_room, name='chat_room'),
    path('chats/', views.chat_list, name='chat_list'),
]