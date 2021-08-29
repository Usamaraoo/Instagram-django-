from django.urls import path
from .views import homepage_view, liked_view,comment_view
urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('liked/', liked_view, name='liked'),
    path('comment/', comment_view, name='comment')
]
