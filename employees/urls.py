
from django.urls import path
from . import views


urlpatterns = [
    path('', views.employees, name='employees'),
    path('employee_create', views.employee_create, name='employee_create'),
    path('employee_reade/<int:id>', views.employee_reade, name='employee_reade'),
    path('employee_update/<int:id>', views.employee_update, name='employee_update'),
    path('employee_delete/<int:id>', views.employee_delete, name='employee_delete'),
    path('ajax/load-regions/', views.load_region, name='load_region'),
    path('ajax/load-states/', views.load_state, name='load_state'),
    path('ajax/load-citys/', views.load_city, name='load_city'),
    path('ajax/load_workSpecialtys/', views.load_workSpecialty, name='load_workSpecialty'),
    path('ajax/load_branchBanks/', views.load_branchBank, name='load_branchBank')
]