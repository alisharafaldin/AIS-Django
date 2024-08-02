from django.urls import path
from . import views 

urlpatterns = [  
    path('', views.invoices, name='invoices_sales'),
    path('invoice_sales_create', views.invoice_sales_create, name='invoice_sales_create'),
    # path('invoice_reade/<int:id>', views.invoice_reade, name='invoice_reade'),
    # path('invoice_update/<int:id>', views.invoice_update, name='invoice_update'),
    # path('invoice_delete/<int:id>', views.invoice_delete, name='invoice_delete'),
]