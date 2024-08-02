from django.urls import path
from . import views 

urlpatterns = [  
    # path('', views.purchases, name='purchases'),
    # path('purchase_create', views.purchase_create, name='purchase_create'),
    # path('purchase_reade/<int:id>', views.purchase_reade, name='purchase_reade'),
    # path('purchase_update/<int:id>', views.purchase_update, name='purchase_update'),
    # path('purchase_delete/<int:id>', views.purchase_delete, name='purchase_delete'),
 
    path('invoices', views.invoices, name='invoices'),
    path('invoice_create', views.invoice_create, name='invoice_create'),
    # path('invoice_reade/<int:id>', views.invoice_reade, name='invoice_reade'),
    # path('invoice_update/<int:id>', views.invoice_update, name='invoice_update'),
    # path('invoice_delete/<int:id>', views.invoice_delete, name='invoice_delete'),
]