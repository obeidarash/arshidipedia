from django.contrib import admin
from django.urls import path
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]
admin.site.site_header = "UMSRA Admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"
