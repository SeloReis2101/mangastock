from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification
from .consumers import NotificationConsumer

def index(request):
    return render(request, 'notification/index.html')

# def test(request):
#     return render(request, 'send_notification.html')

# def notification_list(request):
#     user = request.user
#     notifications = Notification.objects.filter(user=user).order_by('-created_at')
#     params = {'notifications': notifications}
#     return render(request, 'notification_list.html', params)

# def send_notification(request):
#     if request.method == 'POST':
#         message = request.POST.get('message', '')
#         NotificationConsumer().receive(json.dumps({'message': message}))
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})

# def mark_notification_as_read(request, notification_id):
#     notification = Notification.objects.get(id=notification_id)
#     notification.update(read=True)
#     return JsonResponse({'success': True})

# def mark_all_as_read(request):
#     user = request.user
#     Notification.objects.filter(user=user, read=False).update(read=True)
#     return JsonResponse({'success': True})