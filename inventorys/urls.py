from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views 


urlpatterns = [  
    path('', views.product_quantity_summary, name='product_quantity_summary'),
    path('net_sales', views.net_sales, name='net_sales'),
    path('net_sales_search', views.net_sales_search, name='net_sales_search'),
    # path('sold_products', views.sold_products, name='sold_products'),


]  