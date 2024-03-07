from django.utils import timezone
from django.db.models import Avg
from .models import Rating

def time_ago_in_words(created_at):
    now = timezone.now()
    time_difference = now - created_at

    if time_difference.days > 0:
        return f"{time_difference.days}d"
    elif time_difference.seconds >= 3600:
        hours = time_difference.seconds // 3600
        return f"{hours}h"
    elif time_difference.seconds >= 60:
        minutes = time_difference.seconds // 60
        return f"{minutes}m"
    else:
        return f"{time_difference.seconds}s"

def get_manga_rating(manga_id):
    manga_ratings = Rating.objects.filter(manga_id=manga_id)
    average_rating = manga_ratings.aggregate(Avg('rating'))['rating__avg']
    return manga_rating