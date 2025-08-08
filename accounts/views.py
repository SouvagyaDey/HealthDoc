from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import DoctorRegisterForm, PatientRegisterForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from doctors.models import Doctor
from appointments.models import Appointment


def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def doctor_dashboard(request):
    try:
        doctor = Doctor.objects.get(user=request.user)
        appointments = Appointment.objects.filter(doctor=doctor).order_by('-appointment_date', '-appointment_time')
        context = {
            'doctor': doctor,
            'appointments': appointments,
            'pending_appointments': appointments.filter(status='pending').count(),
            'confirmed_appointments': appointments.filter(status='confirmed').count(),
        }
    except Doctor.DoesNotExist:
        context = {'error': 'Doctor profile not found'}
    return render(request, 'doctor_dashboard.html', context)

@login_required
def patient_dashboard(request):
    appointments = Appointment.objects.filter(patient=request.user).order_by('-appointment_date', '-appointment_time')
    doctors = Doctor.objects.all()
    context = {
        'appointments': appointments,
        'doctors': doctors,
        'upcoming_appointments': appointments.filter(status__in=['pending', 'confirmed']).count(),
        'completed_appointments': appointments.filter(status='completed').count(),
    }
    return render(request, 'patient_dashboard.html', context)

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = DoctorRegisterForm()
    return render(request, 'register_doctor.html', {'form': form})

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = PatientRegisterForm()
    return render(request, 'register_patient.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            try:
                profile = Profile.objects.get(user=user)
                if profile.role.lower() == 'doctor':
                    # print("Yes")
                    return redirect('home')
                elif profile.role.lower() == 'patient':
                    return redirect('home') 
                else:
                    return redirect('home')
            except Profile.DoesNotExist:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
