from django.urls import path
from .import views

urlpatterns = [
    path('notifications/', views.index, name="index")
    # path('notifications/', views.notification_list, name='notification_list'),
    # path('send_notification/', views.send_notification, name='send_notification'),
    # path('test/', views.test, name="test"),
]