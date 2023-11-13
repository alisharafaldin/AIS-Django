
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shareholders, name='shareholders'),
    path('shareholder_create', views.shareholder_create, name='shareholder_create'),
    path('shareholder_reade/<int:id>', views.shareholder_reade, name='shareholder_reade'),
    path('shareholder_update/<int:id>', views.shareholder_update, name='shareholder_update'),
    path('shareholder_delete/<int:id>', views.shareholder_delete, name='shareholder_delete'),
    path('shareholder_print/<int:id>', views.shareholder_update, name='shareholder_print'),

    path('contracts', views.contracts, name='contracts'),
    path('contract_create', views.contract_create, name='contract_create'),
    path('contract_reade/<int:id>', views.contract_reade, name='contract_reade'),
    path('contract_update/<int:id>', views.contract_update, name='contract_update'),
    path('contract_delete/<int:id>', views.contract_delete, name='contract_delete'),
    path('contract_print/<int:id>', views.contract_print, name='contract_print'),
]


