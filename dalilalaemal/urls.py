
from django.urls import path
from . import views


urlpatterns = [
    path('', views.dalilalaemal, name='dalilalaemal'),
    path('all', views.dalilalaemal_all, name='dalilalaemal_all'),
    path('home', views.dalilalaemal_home, name='dalilalaemal_home'),
    path('search', views.dalilalaemal_search, name='dalilalaemal_search'),
    path('single/<int:id>', views.dalilalaemal_single, name='dalilalaemal_single'),

]