from django.urls import path
from . import views

urlpatterns = [  
    path('account_new', views.account_new, name='account_new'),
    path('account_view/<int:id>', views.account_view, name='account_view'),
    path('account_update/<int:id>', views.account_update, name='account_update'),
    path('account_delete/<int:id>', views.account_delete, name='account_delete'),
    path('', views.accounts, name='accounts'),
    path('qayd_new', views.qayd_new, name='qayd_new'),
    path('qayd_view/<int:id>', views.qayd_view, name='qayd_view'),
    path('qayd_update/<int:id>', views.qayd_update, name='qayd_update'),
    path('qayd_delete/<int:id>', views.qayd_delete, name='qayd_delete'),
    path('qayds', views.qayds, name='qayds'),
]