from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'reservations'

urlpatterns = [
    path('book_table/', views.book_table, name='book_table'),
    path('booking_success/', views.booking_success, name='booking_success'),  
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('view_bookings/', views.view_bookings, name='view_bookings'),
    path('reservations/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
]
