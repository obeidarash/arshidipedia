from django.contrib import admin
from django.urls import path, include
from .views import home, new_home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home),
    path('', new_home),
    path('tinymce/', include('tinymce.urls')),
]

admin.site.site_header = "Arshidipedia Admin"
admin.site.site_title = "Arshidipedia Admin Portal"
admin.site.index_title = "Welcome to Arshidipedia Researcher Portal"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
