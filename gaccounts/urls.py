from django.urls import path
from . import views

urlpatterns = [  
    # path('test', views.test, name='test'),
    path('acc_all', views.acc_add, name='acc_all'),
    path('acc_update/<int:id>', views.acc_update, name='acc_update'),
    path('qayd_add', views.qayd_add, name='qayd_add'),
    path('qayd_all', views.qayd_all, name='qayd_all'),
    path('qayd_update/<int:id>', views.qayd_update, name='qayd_update'),
    path('qayd_delete/<int:id>', views.qayd_delete, name='qayd_delete'),
    path('qayd_print/<int:id>', views.qayd_print, name='qayd_print'),
]