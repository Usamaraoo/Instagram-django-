from django.urls import path
from .views import (user_profile, signup_view, login_view,
                    post_view, follow_unfollow, following_view,
                    logout_view, follow_ajax, set_dp)

urlpatterns = [
    path('profile/<str:username>', user_profile, name='profile'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('post/', post_view, name='post'),
    path('follow/<int:pk>', follow_unfollow, name='follow_unfollow'),
    path('ajax_follow/', follow_ajax, name='follow_ajax'),
    path('setphoto/', set_dp, name='set_dp'),


    path('follow_view/', following_view, name='followunfollow'),

]
