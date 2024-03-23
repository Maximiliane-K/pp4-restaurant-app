from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
#from .forms import RegistrationForm


@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date_time = form.cleaned_data['date_time']
            num_people = form.cleaned_data['num_people']
            booking = Booking.objects.create(user=request.user, date_time=date_time, num_people=num_people)
            return redirect('reservations:booking_success')
    else:
        form = BookingForm()
    return render(request, 'reservations/book_table.html', {'form': form})


def booking_success(request):
    #return render(request, 'reservations/booking_success.html')

    latest_booking = Booking.objects.latest('id')  # Retrieve the latest booking
    return render(request, 'reservations/booking_success.html', {'latest_booking': latest_booking})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate the user after registration
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect the user to the table booking page after successful registration
                return redirect('reservations:book_table')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def view_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'view_bookings.html', {'user_bookings': user_bookings})


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        booking.delete()
        return redirect('reservations:view_bookings')

    return render(request, 'reservations/confirm_delete_booking.html', {'booking': booking})


def custom_logout(request):
    return render(request, 'custom_logout.html')