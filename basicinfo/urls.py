
from django.urls import path
from . import views


urlpatterns = [
    path('', views.basicinfo, name='basicinfo'),
    path('ajax/load-regions/', views.load_region, name='load_region'),
    path('ajax/load-states/', views.load_state, name='load_state'),
    path('ajax/load-citys/', views.load_city, name='load_city'),
    path('ajax/load_workSpecialtys/', views.load_workSpecialty, name='load_workSpecialty'),
    path('ajax/load_branchBanks/', views.load_branchBank, name='load_branchBank'),
    path('ajax/load_businessScopeSpecializations/', views.load_businessScopeSpecialization, name='load_businessScopeSpecialization')
]


