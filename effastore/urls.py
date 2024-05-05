
from django.urls import path
from . import views


urlpatterns = [
    path('', views.effastore, name='effastore'),
]