from django.urls import path
from . import views

urlpatterns = [  
    # path('test', views.test, name='test'),
    path('acc_all', views.acc_add, name='acc_all'),
    path('acc_update/<int:id>', views.acc_update, name='acc_update'),
    # path('qayd_add', views.qayd_add, name='qayd_add'),
    path('new_qayd', views.new_qayd, name='new_qayd'),
    path('qayds', views.qayds, name='qayds'),
    path('update_qayd/<int:id>', views.update_qayd, name='update_qayd'),
    path('delete_qayd/<int:id>', views.delete_qayd, name='delete_qayd'),
    path('view_qayd/<int:id>', views.view_qayd, name='view_qayd'),
]