from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage/', views.homepage, name='homepage'),
    path('homepage/elms', views.login),
    path('contact/', views.contact, name='contact')
]