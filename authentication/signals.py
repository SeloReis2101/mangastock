from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User
from .other_utils import get_dominant_color

@receiver(pre_save, sender=User)
def update_user_accent_color(sender, instance, **kwargs):
    # Eğer yeni bir profil resmi yükleniyorsa
    if instance.pk is not None:
        try:
            old_user = User.objects.get(pk=instance.pk)
            if old_user.profile_image != instance.profile_image:
                # Profil resmi değiştiği için renk analizi yap
                image_path = instance.profile_image.path
                instance.user_accent_color = get_dominant_color(image_path)
        except User.DoesNotExist:
            pass
    # Eğer user_accent_color henüz ayarlanmamışsa veya kullanıcı yeni bir kullanıcıysa
    if not instance.user_accent_color:
        image_path = instance.profile_image.path
        instance.user_accent_color = get_dominant_color(image_path)
