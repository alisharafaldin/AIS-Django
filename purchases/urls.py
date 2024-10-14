from django.urls import path
from . import views 

urlpatterns = [  
    path('', views.invoices_purchases, name='invoices_purchases'),
    path('purchased_products', views.purchased_products, name='purchased_products'),
    path('purchased_products_search', views.purchased_products_search, name='purchased_products_search'),
    path('invoices_purchases_search', views.invoices_purchases_search, name='invoices_purchases_search'),
    path('invoice_purchases_create', views.invoice_purchases_create, name='invoice_purchases_create'),
    path('supplier_purchases_invoices/<int:supplier_id>', views.supplier_purchases_invoices, name='supplier_purchases_invoices'),
    path('invoice_purchases_reade/<int:id>', views.invoice_purchases_reade, name='invoice_purchases_reade'),
    path('invoice_purchases_update/<int:id>', views.invoice_purchases_update, name='invoice_purchases_update'),
    path('invoice_purchases_delete/<int:id>', views.invoice_purchases_delete, name='invoice_purchases_delete'),
    # path('post_invoice_purchases_to_journal/<int:id>', views.post_invoice_purchases_to_journal, name='post_invoice_purchases_to_journal'),
    # path('invoice/<int:id>/pdf/', views.invoice_pdf, name='invoice_pdf'),

    path('suppliers', views.suppliers, name='suppliers'),
    path('supplier_create', views.supplier_create, name='supplier_create'),
    path('supplier_update/<int:id>', views.supplier_update, name='supplier_update'),
    path('supplier_reade/<int:id>', views.supplier_reade, name='supplier_reade'),
    path('supplier_delete/<int:id>', views.supplier_delete, name='supplier_delete'),
]