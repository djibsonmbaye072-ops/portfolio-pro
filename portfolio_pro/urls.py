from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # 🔧 Admin
    path('admin/', admin.site.urls),

    # 🌐 Routes principales (home + about)
    path('', include('core.urls')),
]


# 📂 Gestion des fichiers MEDIA (images projets)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)