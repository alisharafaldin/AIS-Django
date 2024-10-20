from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
"""ais URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/',include('pages.urls')),
    path('',include('dalilalaemal.urls')),
    path('basicinfo/',include('basicinfo.urls')),
    path('profiles/',include('profiles.urls')),
    path('companys/',include('companys.urls')),
    path('employees/',include('employees.urls')),
    path('products/',include('products.urls')),
    path('inventorys/',include('inventorys.urls')),
    path('sales/',include('sales.urls')),
    path('purchases/',include('purchases.urls')),

    # رابط طلب إعادة تعيين كلمة المرور
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    # رابط لإعلام المستخدم بأن بريد الاستعادة قد أُرسل
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    # رابط إعادة تعيين كلمة المرور باستخدام الرابط المرسل عبر البريد
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    # رابط لإعلام المستخدم بأن كلمة المرور قد تم تغييرها بنجاح
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)