
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.dalilalaemal, name='dalilalaemal'),
    path('', views.dalils, name='dalils'),
    path('home', views.dalil_home, name='dalil_home'),
    path('business_Scope', views.dalils_business_Scope, name='dalils_business_Scope'),
    path('search', views.dalilalaemal_search, name='dalilalaemal_search'),
    path('single/<int:id>', views.dalilalaemal_single, name='dalilalaemal_single'),

    path('create', views.create, name='dalil_create'),
    path('update/<int:id>', views.update, name='update'),
]