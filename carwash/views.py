import datetime
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from carwash.models import Booking, CarWashPlace, CarWashService, BookingStatus


def home(request):
    user = request.user
    print(user)
    bookings = []

    shops = CarWashPlace.objects.all()

    reset_slots_availability(shops)

    if user.is_authenticated:
        bookings = Booking.objects.filter(customer__id=user.id).prefetch_related('customer').select_related('carwash').select_related('status').order_by('-date')
        print(bookings[0])

    context = {
        "page": "Home",
        "user": user,
        "bookings" : bookings,
    }

    return render(request, template_name="carwash/index.html", context=context)


def search(request):
    car_wash_places = []

    search_term = request.GET.get('place')
    view_all = request.GET.get('all')

    if view_all:
        car_wash_places = CarWashPlace.objects.all()

    if search_term:
        car_wash_places = CarWashPlace.objects.filter(name__icontains=search_term)

    print("search_term:", search_term)
    context = {
        "page": 'Search',
        "places": car_wash_places,
        "search": search_term
    }
    return render(request, template_name="carwash/index.html", context=context)


@login_required
def book(request, place_id):
    context = {
        "page": "Book",
        "place_id": place_id
    }

    car_wash_place = CarWashPlace.objects.filter(id=place_id).prefetch_related('services').first()

    if not car_wash_place:
        return redirect(reverse('search') + '?all=1')

    context["place"] = car_wash_place

    services = car_wash_place.services.all() or []

    context["services"] = services

    return render(request, template_name='carwash/book.html', context=context)


@login_required
def book_confirm(request):
    place_id = request.POST.get('place_id')
    service_id = request.POST.get('service_id')

    print(place_id, service_id)
    if not place_id or not service_id:
        return redirect(reverse('search') + '?all=1')

    carwash_place = CarWashPlace.objects.filter(id=place_id).first()
    carwash_place.slots -= 1
    if carwash_place.slots < 0:
        carwash_place.slots = 0
    carwash_place.save()
    service = carwash_place.services.filter(id=service_id).first()
    status = BookingStatus.objects.filter(status__icontains='pending').first()
    booking = Booking(customer=request.user, carwash=carwash_place, service=service, status=status)

    booking.save()

    return redirect('home')


# utilities
def reset_slots_availability(car_wash_shops):

    for shop in car_wash_shops:
        last_refresh = shop.slots_last_refresh

        last_refresh_date = datetime.datetime.strptime(str(last_refresh), "%Y-%m-%d").date()
        now = datetime.datetime.today().date()

        print(last_refresh_date, now)

        print(last_refresh_date > now)

        print(now > last_refresh_date)

        if now > last_refresh_date:
            default_numberof_slots = CarWashPlace._meta.get_field('slots').get_default()
            shop.slots = default_numberof_slots
            shop.slots_last_refresh = now
            shop.save()
