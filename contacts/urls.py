from .views import company
from django.urls import path

urlpatterns = [
    path('company/<int:company_id>/', company, name='company'),
]
