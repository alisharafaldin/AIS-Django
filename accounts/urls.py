from django.urls import path
from . import views 
from .views import qaydCreate, qaydDetail, qaydUpdate, qaydList, qaydDelete

# app_name = 'ais_qayd'

urlpatterns = [  
    path('', views.accounts, name='accounts'),
    path('account_create', views.account_create, name='account_create'),
    path('account_reade/<int:id>', views.account_reade, name='account_reade'),
    path('account_update/<int:id>', views.account_update, name='account_update'),
    path('account_delete/<int:id>', views.account_delete, name='account_delete'),
    
    path('qayd_create', qaydCreate.as_view(), name='qayd_create'),
    path('qayd_detail/<int:pk>', qaydDetail.as_view(), name='qayd_detail'),
    path('qayd_update/<int:pk>', views.qaydUpdate.as_view(), name='qayd_update'),
    path('qayd_delete/<int:pk>',qaydDelete.as_view(), name='qayd_delete'),
    path('qayd_list', qaydList.as_view(), name='qayd_list'),

    # path('qayd_create', views.qayd_create, name='qayd_create'),
    # path('qayd_reade/<int:id>', views.qayd_reade, name='qayd_reade'),
    # path('qayd_update/<int:id>', views.qayd_update, name='qayd_update'),
    # path('qayd_delete/<int:id>', views.qayd_delete, name='qayd_delete'),
    path('qayds', views.qayds, name='qayds'),
]