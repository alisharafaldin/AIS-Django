
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shareholders, name='hadena_shareholders'),
    path('shareholder/<int:shareholder_id>', views.shareholder, name='hadena_shareholder'),
    path('share_update/<int:shareholder_id>', views.share_update, name='hadena_share_update'),
    path('share_delete/<int:shareholder_id>', views.share_delete, name='hadena_share_delete'),
    path('contracts', views.contracts, name='hadena_contracts'),
    path('contract/<int:contract_id>', views.contract, name='hadena_contract'),
    path('update/<int:contract_id>', views.update, name='hadena_update'),
    path('pdf/<int:contract_id>', views.pdf, name='hadena_pdf'),
]