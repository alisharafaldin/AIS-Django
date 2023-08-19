from django.contrib import admin
from django.urls import path , include
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('' , include('pages.urls')),
    # path('users/' , include('users.urls')),
    path('basicinfo/',include('basicinfo.urls')),
    path('hadena/',include('hadena.urls')),
    path('forex/',include('forex.urls')),
    path('gaccounts/',include('gaccounts.urls')),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
    path('orders/',include('orders.urls')),
    path('employees/',include('employees.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
