from django.urls import path
from . import views

urlpatterns = [
    path('', views.items, name='products'),
    path('<int:pro_id>', views.items, name='product'),
    path('search', views.search, name='search'),
]