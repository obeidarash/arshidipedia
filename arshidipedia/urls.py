from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('tinymce/', include('tinymce.urls')),
]
admin.site.site_header = "Arshidipedia Admin"
admin.site.site_title = "Arshidipedia Admin Portal"
admin.site.index_title = "Welcome to Arshidipedia Researcher Portal"
