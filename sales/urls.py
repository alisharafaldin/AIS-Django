from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views 

router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)

urlpatterns = [  
    path('api/', include(router.urls)),
    path('', views.invoices_sales, name='invoices_sales'),
    path('sold_products', views.sold_products, name='sold_products'),
    path('sold_products_search', views.sold_products_search, name='sold_products_search'),
    path('invoices_sales_search', views.invoices_sales_search, name='invoices_sales_search'),
    path('invoice_sales_create', views.invoice_sales_create, name='invoice_sales_create'),
    path('customer_sales_invoices/<int:customer_id>', views.customer_sales_invoices, name='customer_sales_invoices'),
    path('invoice_sales_reade/<int:id>', views.invoice_sales_reade, name='invoice_sales_reade'),
    path('invoice_sales_update/<int:id>', views.invoice_sales_update, name='invoice_sales_update'),
    path('invoice_sales_delete/<int:id>', views.invoice_sales_delete, name='invoice_sales_delete'),
    path('post_invoice_sales_to_journal/<int:id>', views.post_invoice_sales_to_journal, name='post_invoice_sales_to_journal'),
    # path('invoice/<int:id>/pdf/', views.invoice_pdf, name='invoice_pdf'),

    path('customers', views.customers, name='customers'),
    path('customer_create', views.customer_create, name='customer_create'),
    path('customer_update/<int:id>', views.customer_update, name='customer_update'),
    path('customer_reade/<int:id>', views.customer_reade, name='customer_reade'),
    path('customer_delete/<int:id>', views.customer_delete, name='customer_delete'),

]  