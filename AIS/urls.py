from django.contrib import admin
from django.urls import path , include
from django.conf import settings 
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('dalilalaemal.urls')),
    path('basicinfo/',include('basicinfo.urls')),
    path('hadena/',include('hadena.urls')),
    path('forex/',include('forex.urls')),
    path('profiles/',include('profiles.urls')),
    path('accounts/',include('accounts.urls')),
    path('sales/',include('sales.urls')),
    path('products/',include('products.urls')),
    path('orders/',include('orders.urls')),
    path('employees/',include('employees.urls')),
    path('companys/',include('companys.urls')),
    path('pages/',include('pages.urls')),
    path('purchases/',include('purchases.urls')),
    path('inventorys/',include('inventorys.urls')),
    path('cashreceipt/',include('cashreceipt.urls')),
    
] 
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
