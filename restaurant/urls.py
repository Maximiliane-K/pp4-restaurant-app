from django.urls import path
from . import views


app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('food/', views.foodmenu, name='food'),
    path('drink/', views.beveragemenu, name='drink'),
    path('contact/', views.contact, name='contact'),
]