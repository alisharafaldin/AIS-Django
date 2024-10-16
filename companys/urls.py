
from django.urls import path
from . import views


urlpatterns = [
    path('', views.companys, name='companys'),
    path('company_create', views.company_create, name='company_create'),
    path('company_reade/<int:id>', views.company_reade, name='company_reade'),
    path('company_update/<int:id>', views.company_update, name='company_update'),
    path('company_delete/<int:id>', views.company_delete, name='company_delete'),
    path('switch_company/<int:company_id>/', views.switch_company, name='switch_company'),
    
    path('tonavbar', views.tonavbar, name='tonavbar'),
]