from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views 


urlpatterns = [  
    path('', views.product_quantity_summary, name='product_quantity_summary'),
    # path('sold_products', views.sold_products, name='sold_products'),


]  