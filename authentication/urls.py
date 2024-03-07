from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('profile/<str:username>', views.profile, name="profile"),
    path('send_follow_request/', views.follow_request, name="send_follow_request"),
    path('unfollow/', views.unfollow, name="unfollow"),
]