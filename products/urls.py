from django.urls import path
from . import views

urlpatterns = [
    path('', views.itemsDetails, name='products'),
    path('<int:pro_id>', views.itemDetails, name='product'),
    path('search', views.search, name='search'),
]