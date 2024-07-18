from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView

urlpatterns = [  
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('user_reade', views.user_reade, name='user_reade'),
    path('pro_fav/<int:pro_id>', views.pro_fav, name='pro_fav'),
    path('show_pro_fav', views.show_pro_fav, name='show_pro_fav'),

    path('reset_password/', CustomPasswordResetView.as_view(template_name="registration/password_reset.html"), name="reset_password"),
    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name='profiles/registration/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_complete'),

]