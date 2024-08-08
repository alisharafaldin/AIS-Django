from django.urls import path
from . import views 

urlpatterns = [  
    path('', views.invoices_sales, name='invoices_sales'),
    path('invoice_sales_create', views.invoice_sales_create, name='invoice_sales_create'),
    path('invoice_sales_reade/<int:id>', views.invoice_sales_reade, name='invoice_sales_reade'),
    path('invoice_sales_update/<int:id>', views.invoice_sales_update, name='invoice_sales_update'),
    path('invoice_sales_delete/<int:id>', views.invoice_sales_delete, name='invoice_sales_delete'),

    path('customers', views.customers, name='customers'),
    path('customer_create', views.customer_create, name='customer_create'),
    path('customer_update/<int:id>', views.customer_update, name='customer_update'),
    path('customer_reade/<int:id>', views.customer_reade, name='customer_reade'),
    path('customer_delete/<int:id>', views.customer_delete, name='customer_delete'),

]