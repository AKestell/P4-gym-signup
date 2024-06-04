from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),  # Ensure this line exists
    path('bookings/', views.BookingListView.as_view(), name='booking-list'),
    path('cancel/', views.cancel, name='cancel'),
    path('bookings/', views.bookings_list, name='bookings-list'),
    path('bookings/create/', views.create_booking, name='create-booking'),
    path('bookings/<int:pk>/', views.booking_detail, name='booking-detail'),
    path('bookings/<int:pk>/update/', views.update_booking, name='update-booking'),
    path('bookings/<int:pk>/delete/', views.delete_booking, name='delete-booking'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup_view, name='signup'),
]