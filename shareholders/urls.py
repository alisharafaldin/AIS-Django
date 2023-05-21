
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shareholders, name='shareholders'),
    path('shareholder/<int:shareholder_id>', views.shareholder, name='shareholder'),
    path('share_update/<int:shareholder_id>', views.share_update, name='share_update'),
    path('share_delete/<int:shareholder_id>', views.share_delete, name='share_delete'),
    path('contracts', views.contracts, name='contracts'),
    path('contract/<int:contract_id>', views.contract, name='contract'),
    path('update/<int:contract_id>', views.update, name='update'),
    path('pdf/', views.pdf, name='pdf'),
]