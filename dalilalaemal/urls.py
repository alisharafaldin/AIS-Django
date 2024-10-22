from django.urls import path
from . import views

urlpatterns = [
    # path('', views.dalilalaemal, name='dalilalaemal'),
    path('', views.dalil_home, name='dalil_home'),
    path('add_dalil', views.add_dalil, name='add_dalil'),
    path('dalils', views.dalils, name='dalils'),
    path('business_Scope', views.dalils_business_Scope, name='dalils_business_Scope'),
    path('cities', views.dalil_cities, name='dalil_cities'),
    path('search', views.dalil_search, name='dalil_search'),
    path('single/<int:id>', views.dalil_single, name='dalil_single'),

    path('create', views.create, name='dalil_create'),
    path('update/<int:id>', views.update, name='update'),

    path('the_four_freedoms_view', views.the_four_freedoms_view, name='the_four_freedoms_view'),
]