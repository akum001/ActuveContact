from django.urls import path
from .views import index, contact_us, about_us, services

urlpatterns = [
    path('', index, name='home'),
    path('email/', contact_us, name='email'),
    path('about/', about_us, name='about_us'),
    path('services/', services, name='services')
]
