from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app_users.urls')),
    path('', include('homepage.urls')),

    path('social-auth/', include('social_django.urls', namespace="social")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
