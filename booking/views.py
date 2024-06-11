from django.shortcuts import render, redirect
from django.views import generic
from .models import Booking
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.contrib.auth.forms import UserCreationForm
from django_summernote.admin import SummernoteModelAdmin


# Create your views here.
class BookingListView(generic.ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'

def home(request):
    return render(request, 'booking/index.html')

def cancel(request):
    # This view handles the cancellation logic.
    # For now, it just redirects to the homepage as a placeholder.
    return redirect('index')

def book(request):
    # Your view logic here
    return render(request, 'booking/book.html')

from .forms import BookingForm

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  
            booking.save()
            return redirect('booking-detail', pk=booking.pk)
    else:
        form = BookingForm()
    return render(request, 'booking/create_booking.html', {'form': form})

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking/booking_detail.html', {'booking': booking})

def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking-detail', pk=booking.pk)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/update_booking.html', {'form': form})

@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.user == booking.user:  
        booking.delete()
        return redirect('bookings-list')
    else:
        return redirect('booking-detail', pk=pk)  

class BookingAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)  

def bookings_list(request):
    bookings = Booking.objects.all()  
    hours = range(9, 17, 2)  
    time_slots = [f"{hour}:00 - {hour + 1}:00" for hour in hours]
    context = {
        'bookings': bookings,
        'time_slots': time_slots
    }
    return render(request, 'booking/bookings_list.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'booking/signup.html', {'form': form})


def login_view(request):
    # Your view logic here
    return render(request, 'booking/login.html')
