from django.urls import path
from .views import home, publications, about_us

urlpatterns = [
    path('', home, name='home'),
    path('publications/', publications, name='publications'),
    path('about_us/', about_us, name='about_us'),
]