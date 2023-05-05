
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shareholders, name='shareholders'),
    path('contracts', views.contracts, name='contracts'),
    path('contract/<int:contract_id>', views.contract, name='contract'),
    path('update/<int:contract_id>', views.update, name='update'),
]