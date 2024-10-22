from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile', views.profile, name='profile'),
    path('profile_update/<int:id>/', views.profile_update, name='profile_update'),
    path('logout', views.logout, name='logout'),
    path('user_reade', views.user_reade, name='user_reade'),
    path('show_pro_fav', views.show_pro_fav, name='show_pro_fav'),

    path('password_reset/', CustomPasswordResetView.as_view(template_name="profiles/registration/password_reset.html"), name="reset_password"),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='profiles/registration/password_reset.html'), name='password_reset'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='profiles/registration/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='profiles/registration/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='profiles/registration/password_reset_done.html'), name='password_reset_complete'),
]