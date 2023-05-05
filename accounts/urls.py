from django.urls import path
from . import views

urlpatterns = [  
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('signup', views.singup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('pro_fav/<int:pro_id>', views.pro_fav, name='pro_fav'),
    path('show_pro_fav', views.show_pro_fav, name='show_pro_fav'),
]