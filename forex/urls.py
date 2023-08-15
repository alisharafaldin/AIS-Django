from django.urls import path
from . import views

urlpatterns = [
    path('', views.shareholders, name='forex_shareholders'),
    path('shareholder/<int:shareholder_id>', views.shareholder, name='forex_shareholder'),
    path('share_update/<int:shareholder_id>', views.share_update, name='forex_share_update'),
    path('share_delete/<int:shareholder_id>', views.share_delete, name='forex_share_delete'),
    path('contracts', views.contracts, name='forex_contracts'),
    path('contract/<int:contract_id>', views.contract, name='forex_contract'),
    path('update/<int:contract_id>', views.update, name='forex_update'),
    path('pdf/<int:contract_id>', views.pdf, name='forex_pdf'),
]