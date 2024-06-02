from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.BookingListView.as_view(), name='booking-list'),
    path('book/', views.book, name='book'),
    path('cancel/', views.cancel, name='cancel'),
]