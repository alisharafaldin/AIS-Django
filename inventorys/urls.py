from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views 
from . import reports


urlpatterns = [  

    path('', views.inventorys, name='inventorys'),
    path('inventorys_search', views.inventorys_search, name='inventorys_search'),
    path('inventory_create', views.inventory_create, name='inventory_create'),
    path('inventory_reade/<int:id>', views.inventory_reade, name='inventory_reade'),
    path('inventory_update/<int:id>', views.inventory_update, name='inventory_update'),
    path('inventory_delete/<int:id>', views.inventory_delete, name='inventory_delete'),

    path('item_quantity_summary', reports.item_quantity_summary, name='item_quantity_summary'),
    path('net_sales', reports.net_sales, name='net_sales'),
    path('net_sales_search', reports.net_sales_search, name='net_sales_search'),
    # path('sold_products', views.sold_products, name='sold_products'),


]  