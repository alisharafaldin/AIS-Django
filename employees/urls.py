
from django.urls import path
from . import views


urlpatterns = [
    path('', views.employees, name='employees'),
    path('employee_create', views.employee_create, name='employee_create'),
    path('employee_reade/<int:id>', views.employee_reade, name='employee_reade'),
    path('employee_update/<int:id>', views.employee_update, name='employee_update'),
    path('employee_delete/<int:id>', views.employee_delete, name='employee_delete'),
]