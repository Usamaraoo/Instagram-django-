from django.urls import path
from .views import homepage_view, liked_view, comment_view, notification_view, explore_view, post_detail, add_story
urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('liked/', liked_view, name='liked'),
    path('comment/', comment_view, name='comment'),
    path('notifications/', notification_view, name='notifications'),
    path('explore/', explore_view, name='explore'),
    path('post/<int:pk>', post_detail, name='post_detail'),
    path('add/story/', add_story, name='add_story')

]
