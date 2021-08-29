from django.urls import path
from .views import (user_profile, signup_view, login_view,
                    post_view, follow_unfollow)

urlpatterns = [
    path('profile/<str:username>', user_profile, name='profile'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('post/', post_view, name='post'),
    path('follow/<int:pk>', follow_unfollow, name='follow_unfollow'),

]
