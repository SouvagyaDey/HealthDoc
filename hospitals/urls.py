from django.contrib import admin
from django.urls import path
from hospitals.views import hospital_list, hospital_details,home,book_appointment


urlpatterns = [
    path('', home, name='home'),
    path('hospitals/', hospital_list, name='hospital_list'),
    path('book-appointment/', book_appointment, name='book_appointment'),
    path('hospitals/<int:hospital_id>/', hospital_details, name='hospital_details'),
]
