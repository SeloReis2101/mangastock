from django.db import models
from authentication.models import User

# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     read = models.BooleanField(default=False)

class Notification(models.Model):
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.message