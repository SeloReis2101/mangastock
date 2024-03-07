from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chat, Message

@login_required
def chat_room(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = chat.messages.all()
    params = {'chat': chat, 'messages': messages}
    return render(request, 'chat/chat_room.html', params)

@login_required
def chat_list(request):
    chats = Chat.objects.filter(user1=request.user) | Chat.objects.filter(user2=request.user)
    params = {'chats': chats }
    return render(request, 'chat/chat_list.html', params)