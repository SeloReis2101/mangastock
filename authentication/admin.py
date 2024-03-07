from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role, FollowRequest, SocialLink

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'fullname', 'email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('fullname', 'username', 'email', 'password')}),
        ('Personal info', {'fields': ('bio', 'banner_image', 'profile_image', 'settings', 'social_links', 'following', 'roles', 'user_accent_color',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('fullname', 'username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'bio', 'banner_image', 'profile_image', 'settings','social_links','following','roles', 'user_accent_color',)}
         ),
    )
    search_fields = ('fullname', 'username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(FollowRequest)
admin.site.register(SocialLink)
admin.site.register(Role)