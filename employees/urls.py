
from django.urls import path
from . import views


urlpatterns = [
    path('', views.employees, name='employees'),
    path('new_emp', views.new_emp, name='new_emp'),
    path('view_emp/<int:id>', views.view_emp, name='view_emp'),
    path('update_emp/<int:id>', views.update_emp, name='update_emp'),
    path('delete_emp/<int:id>', views.delete_emp, name='delete_emp'),
]