from django.urls import path
from .views import invoice

urlpatterns = [
    path('<int:invoice_id>', invoice, name='invoice'),
]
