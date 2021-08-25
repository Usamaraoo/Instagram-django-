from django.urls import path
from .views import (user_profile, signup_view, login_view)

urlpatterns = [
    path('profile/', user_profile, name='profile'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),

]
