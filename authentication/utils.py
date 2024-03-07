from .models import User, FollowRequest

from PIL import Image
import colorsys

def is_following(user, target_user):
    return user.following.filter(id=target_user.id).exists()

def is_follow_request_sent(user, target_user):
    return FollowRequest.objects.filter(from_user=user, to_user=target_user).exists()

def follow(user, target_user):
    if user != target_user and not is_following(user, target_user):
        user.following.add(target_user)

def unfollow(user, target_user):
    if is_following(user, target_user):
        user.following.remove(target_user)

def send_follow_request(from_user, to_user):
    follow_request = FollowRequest.objects.create(from_user=from_user, to_user=to_user)
    return follow_request












# def get_accent_color(profile_image):
#     # Resmi indirin
#     response = requests.get(profile_image.url)
#     image = Image.open(BytesIO(response.content))
#     # Resmi RGB moduna dÃ¶nÃ¼ÅtÃ¼r
#     rgb_image = image.convert('RGB')
#     # Resmin boyutlarÄ±nÄ± alÄ±n
#     width, height = rgb_image.size
#     # Renkleri saklamak iÃ§in bir sÃ¶zlÃ¼k oluÅturun
#     colors = {}
#     # Her pikselde dolaÅarak renkleri sayÄ±n
#     for x in range(width):
#         for y in range(height):
#             pixel_color = rgb_image.getpixel((x, y))
#             # Renkleri sayÄ±n
#             if pixel_color not in colors:
#                 colors[pixel_color] = 1
#             else:
#                 colors[pixel_color] += 1
#     # En sÄ±k kullanÄ±lan renkleri bulun
#     most_common_colors = sorted(colors, key=colors.get, reverse=True)[:3]
#     for color in most_common_colors:
#         # Ãrnek bir kriter: Renklerin toplam deÄerleri 300'den bÃ¼yÃ¼kse arka plan rengi olarak kabul edin
#         if sum(color) > 300:
#             background_color = "#{:02x}{:02x}{:02x}".format(*color)  # RGB tuple'Ä±nÄ± hexadecimal stringe dÃ¶nÃ¼ÅtÃ¼rÃ¼n
#             break
#         else:
#             # HiÃ§bir uygun renk bulunamazsa varsayÄ±lan olarak beyaz kullanÄ±n
#             background_color = '#FFFFFF'
            
#     return background_color


# Kullanımlar:

# # Takip isteği göndermek
# from_user = CustomUser.objects.get(username='sender_username')
# to_user = CustomUser.objects.get(username='recipient_username')
# follow_request = FollowRequest.objects.create(from_user=from_user, to_user=to_user)

# # Takip isteğini kabul etmek veya reddetmek
# follow_request.accept()  # Takip isteğini kabul et
# # veya
# follow_request.reject()  # Takip isteğini reddet

# # Takipçi sayısını güncellemek
# user.following.add(another_user)
# another_user.followers_count += 1
# another_user.save()

# # Takip edilen sayısını güncellemek
# user.followers.add(another_user)
# user.following_count += 1
# user.save()
