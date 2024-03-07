from django.urls import path
from .import views

urlpatterns = [
    path('view_comment/<int:comment_id>', views.view_comment, name="view_comment"),
    path('add_comment/', views.add_comment, name="add_comment"),
    path('add_reply_comment/', views.add_reply_comment, name="add_reply_comment"),
    path('like_comment/<int:comment_id>', views.like_comment, name="like_comment"),
    path('like_reply_comment/<int:reply_id>', views.like_reply_comment, name="like_reply_comment"),
]
