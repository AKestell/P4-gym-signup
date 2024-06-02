from django.shortcuts import render
from django.views.generic import ListView
from .models import Booking

# Create your views here.
class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'


def index(request):
    # This view renders the homepage.
    return render(request, 'index.html')


def cancel(request):
    # This view handles the cancellation logic.
    # For now, it just redirects to the homepage as a placeholder.
    return redirect('index')


def book(request):
    # Your view logic here
    return render(request, 'book.html')