from django.urls import path
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
]