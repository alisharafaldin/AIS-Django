
from django.urls import path
from . import views


urlpatterns = [
    path('', views.dalilalaemal, name='dalilalaemal'),
    path('dalilalaemal_search', views.dalilalaemal_search, name='dalilalaemal_search'),

]