from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from authentication.models import User

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    time_ago = models.CharField(max_length=5, default="", blank=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    
    def __str__(self):
        return f'Comment: {self.user.username} - {self.text[:20]}...'

class CommentReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    time_ago = models.CharField(max_length=5, default="", blank=True)
    likes = models.ManyToManyField(User, related_name='reply_likes', blank=True)
    
    def __str__(self):
        return f'this is reply of {self.user.username} - {self.text[:20]}...'