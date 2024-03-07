from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import login as auth_login
from .import utils as profile_utils

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def profile(request, username):
    user = User.objects.get(username=username)
    is_following = profile_utils.is_following(request.user, user)
    is_follow_request_sent = profile_utils.is_follow_request_sent(request.user, user)
    params = {'user': user, 'is_following': is_following, 'is_follow_request_sent': is_follow_request_sent,}
    return render(request, 'auth/profile.html', params)


def follow_request(request):
    if request.method == 'GET':
        target_username = request.GET['target_username']
        target_user = User.objects.get(username=target_username)
        profile_utils.send_follow_request(request.user, target_user)

    params = {'success': 'Ok'}
    return JsonResponse(params)

def unfollow(request):
    if request.method == 'GET':
        target_username = request.GET['target_username']
        target_user = User.objects.get(username=target_username)
        profile_utils.unfollow(request.user, target_user)

    params = {'success': 'Ok'}
    return JsonResponse(params)