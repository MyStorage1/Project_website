from django.urls import path
from django.contrib.auth import views as auth_view

from . import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),  # FIXME

    path('', views.home, name='home'),
    path('publications/', views.publications, name='publications'),
    path('about_us/', views.about_us, name='about_us'),

    path('user_page/', views.user_page, name='user_page'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('account_settings/', views.account_settings, name='account_settings'),

    path('reset_password/', auth_view.PasswordResetView.as_view(template_name='main_app/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(template_name='main_app/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='main_app/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='main_app/password_reset_done.html'),
         name='password_reset_complete'),

]