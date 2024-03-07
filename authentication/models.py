from django.contrib.auth.models import AbstractUser
from django.db import models

from .other_utils import get_dominant_color

class User(AbstractUser):
    fullname = models.CharField(max_length=100, null=True)
    bio = models.CharField(max_length=100, blank=True)
    banner_image = models.ImageField(upload_to='banner', null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile')
    settings = models.JSONField(default=dict, blank=True)
    social_links = models.ManyToManyField('SocialLink', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    roles = models.ManyToManyField('Role', blank=True)
    user_accent_color = models.CharField(max_length=7, default='#FFFFFF')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Kullanıcının profil fotoğrafının olduğu yolu belirleyin
        image_path = self.profile_image.path

        # Profil fotoğrafındaki dominant rengi alın
        accent_color = get_dominant_color(image_path)

        # Kullanıcının user_accent_color alanını güncelleyin
        self.user_accent_color = accent_color

        # Kullanıcı modelini tekrar kaydedin
        super().save(*args, **kwargs)



class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FollowRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_requests_received')
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def accept(self):
        self.to_user.followers.add(self.from_user)
        self.from_user.following.add(self.to_user)
        self.accepted = True
        self.save()

    def reject(self):
        self.delete()

    def __str__(self):
        return f"{self.from_user} sent a follow request to {self.to_user}"

class SocialLink(models.Model):
    SOCIAL_MEDIA_CHOICES = [
        ('yt', 'YouTube'),
        ('ig', 'Instagram'),
        ('tw', 'Twitch'),
        ('sp', 'Spotify'),
    ]
    social_media = models.CharField(max_length=2, choices=SOCIAL_MEDIA_CHOICES)
    url = models.URLField()

