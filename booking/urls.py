from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.BookingListView.as_view(), name='booking-list'),
    path('cancel/', views.cancel, name='cancel'),
]