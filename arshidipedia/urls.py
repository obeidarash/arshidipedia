from django.contrib import admin
from django.urls import path, include
from .views import new_home, search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', new_home),
    path('tinymce/', include('tinymce.urls')),
    path('invoice/', include('sell.urls')),
    path('search/', search, name='search'),
]

admin.site.site_header = "Arshidipedia Admin"
admin.site.site_title = "Arshidipedia Admin Portal"
admin.site.index_title = "Welcome to Arshidipedia Researcher Portal"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
