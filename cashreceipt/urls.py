
from django.urls import path
from . import views


urlpatterns = [
    path('', views.cashreceipts, name='cashreceipts'),
    path('create', views.cashreceipt_create, name='cashreceipt_create'),
    # path('reade/<int:id>', views.reade, name='reade'),
    # path('update/<int:id>', views.update, name='update'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('switch_company/<int:company_id>/', views.switch_company, name='switch_company'),
]