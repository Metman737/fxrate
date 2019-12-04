from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

import home

urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('', home.views.index)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
