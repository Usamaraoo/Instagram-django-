from django.urls import path
from .views import homepage_view, liked_view
urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('liked/<int:pk>', liked_view, name='liked')
]
