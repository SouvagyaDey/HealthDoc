from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
    path('register/doctor/', views.register_doctor, name='register_doctor'),
    path('register/patient/', views.register_patient, name='register_patient'),
    path('login/', views.user_login, name='login'),
    path('dashboard/doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
]
