
from django.urls import path
from . import views

urlpatterns = [
    path('new', views.shareholder_new, name='shareholder_new'),
    path('view/<int:id>', views.shareholder_view, name='shareholder_view'),
    path('update/<int:id>', views.shareholder_update, name='shareholder_update'),
    path('delete/<int:id>', views.shareholder_delete, name='shareholder_delete'),
    path('print/<int:id>', views.shareholder_update, name='shareholder_print'),
    path('', views.shareholders, name='shareholders'),

    path('contract_new', views.contract_new, name='contract_new'),
    path('contract_view/<int:id>', views.contract_view, name='contract_view'),
    path('contract_update/<int:id>', views.contract_update, name='contract_update'),
    path('contract_delete/<int:id>', views.contract_delete, name='contract_delete'),
    path('contracts', views.contracts, name='contracts'),
    # path('pdf/<int:contract_id>', views.contract_pdf, name='contract_pdf'),
]


