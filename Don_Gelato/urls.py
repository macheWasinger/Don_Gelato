from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import inicio

urlpatterns = [
    path('', inicio, name="inicio"),
    path('', include('core.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('oauth/', include('social_django.urls', namespace='social')),
]

admin.site.site_header = "Administración de Don Gelato"
admin.site.index_title = "Módulos de administración"
admin.site.site_title = "Don Gelato"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
