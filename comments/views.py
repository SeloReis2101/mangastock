from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from .models import Comment, CommentReply
from authentication.models import User
from main.models import Manga, Chapter

from main.utils import time_ago_in_words

def view_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.time_ago = time_ago_in_words(comment.created_at)
    comment.save()
    for reply in comment.replies.all():
        reply.time_ago = time_ago_in_words(reply.created_at)
        reply.save()
    params = {'comment': comment}
    return render(request, 'reply-comment.html', params)

def add_comment(request):
    content_type = request.GET.get('content_type')
    object_id = request.GET.get('object_id')
    user = request.user
    text = request.GET.get('text')

    try:
        content_type = ContentType.objects.get(model=content_type)
        comment = Comment.objects.create(content_type=content_type, object_id=object_id, user=user, text=text)
        comment.save()
        params = {
            'id': comment.id,
            'comment': comment.text, 
            'username': comment.user.username, 
            'fullname': comment.user.fullname,
            'profile_image': user.profile_image.url
        }
        return JsonResponse(params)
    except ContentType.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Invalid content type.'}, status=400)

def add_reply_comment(request):
    parent_id = request.POST.get('parent_id')
    user = request.user
    text = request.POST.get('text')

    try:
        parent = Comment.objects.get(pk=parent_id)
        reply = CommentReply.objects.create(parent=parent, user=user, text=text)
        params = {
            'id': reply.id,
            'comment': reply.text, 
            'username': reply.user.username, 
            'fullname': reply.user.fullname,
            'profile_image': user.profile_image
        }
        return JsonResponse(params)
    except Comment.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Parent comment does not exist.'}, status=400)

def like_comment(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
        user = request.user

        if user in comment.likes.all():
            comment.likes.remove(user)
            liked = False
        else:
            comment.likes.add(user)
            liked = True
        
        return JsonResponse({'liked': liked, 'count': comment.likes.count()})
    except Comment.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Comment does not exist.'}, status=400)

def like_reply_comment(request, reply_id):
    try:
        reply = CommentReply.objects.get(pk=reply_id)
        user = request.user

        if user in reply.likes.all():
            reply.likes.remove(user)
            liked = False
        else:
            reply.likes.add(user)
            liked = True
        
        return JsonResponse({'liked': liked, 'count': reply.likes.count()})
    except CommentReply.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Reply comment does not exist.'}, status=400)