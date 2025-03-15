from django.urls import path
from .views import ItemUpdate

urlpatterns = [
    path('products/bulk/', ItemUpdate.as_view(), name='product-bulk'),
]