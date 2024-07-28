
from django.urls import path
from . import views


urlpatterns = [
    path('', views.basicinfo, name='basicinfo'),
    path('ajax/load-regions/', views.load_region, name='load_region'),
    path('ajax/load-states/', views.load_state, name='load_state'),
    path('ajax/load-citys/', views.load_city, name='load_city'),
    path('ajax/load_workSpecialtys/', views.load_workSpecialty, name='load_workSpecialty'),
    path('ajax/load_branchBanks/', views.load_branchBank, name='load_branchBank')
    # path('generalsettings', views.generalsettings, name='generalsettings'),
    # path('countrie', views.countrie ,name='countrie'),
    # path('edit_countrie/<countrie_id>', views.edit_countrie ,name='edit_countrie'),
    # path('delete_countrie/<countrie_id>', views.delete_countrie ,name='delete_countrie'),
    # path('gender', views.gender ,name='gender'),
    # path('add_gender', views.add_gender ,name='add_gender'),
    # path('edit/<int:gender_id>', views.edit_gender ,name='edit_gender'),
    # path('delete/<int:gender_id>', views.delete_gender ,name='delete_gender'),  
    # path('sponser', views.sponser ,name='sponser'),  
    # path('add_sponser', views.add_sponser ,name='add_sponser'),
]


