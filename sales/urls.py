from django.urls import path
from . import views 

urlpatterns = [  
    path('', views.invoices_sales, name='invoices_sales'),
    path('create_invoice_sales', views.create_invoice_sales, name='create_invoice_sales'),
    path('reade_invoice_sales/<int:id>', views.reade_invoice_sales, name='reade_invoice_sales'),
    path('update_invoice_sales/<int:id>', views.update_invoice_sales, name='update_invoice_sales'),
    path('delete_invoice_sales/<int:id>', views.delete_invoice_sales, name='delete_invoice_sales'),

    path('customers', views.customers, name='customers'),
    path('customer_create', views.customer_create, name='customer_create'),
    path('customer_update/<int:id>', views.customer_update, name='customer_update'),
    path('customer_reade/<int:id>', views.customer_reade, name='customer_reade'),
    path('customer_delete/<int:id>', views.customer_delete, name='customer_delete'),

]