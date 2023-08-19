
from django.urls import path
from . import views


urlpatterns = [
    path('', views.employees, name='employees'),
    path('emp/<int:emp_id>', views.employee, name='employee'),
    path('<int:id>', views.update, name='update_emp'),
]