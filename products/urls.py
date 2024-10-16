from django.urls import path
from . import views

urlpatterns = [
    path('', views.items, name='items'),
    path('items_search', views.items_search, name='items_search'),
    path('item_create', views.item_create, name='item_create'),
    path('item_reade/<int:id>', views.item_reade, name='item_reade'),
    path('item_update/<int:id>', views.item_update, name='item_update'),
    path('item_delete/<int:id>', views.item_delete, name='item_delete'),
]