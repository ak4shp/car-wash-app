from django.urls import path

import carwash.views as views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("book/<int:place_id>/", views.book, name="book_car_wash"),
    path("booking-confirmed/", views.book_confirm, name="book_confirm"),
]
