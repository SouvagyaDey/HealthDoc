from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, Http404
from .forms import AppointmentForm
from .models import Appointment
from doctors.models import Doctor

@login_required
def book_appointment(request):
    doctor_id = request.GET.get('doctor')
    doctors = Doctor.objects.all()
    initial = {}

    if doctor_id:
        initial['doctor'] = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.doctor = get_object_or_404(Doctor, id=request.POST.get('doctor'))
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('patient_dashboard')
    else:
        form = AppointmentForm(initial=initial)

    context = {
        'form': form,
        'doctors': doctors,
        'selected_doctor_id': int(doctor_id) if doctor_id else None
    }
    return render(request, 'book_appointment.html', context)


def appointment_list(request):
    if request.user.is_authenticated:
        doctor = Doctor.objects.filter(user=request.user).first()
        if doctor:
            appointments = Appointment.objects.filter(doctor=doctor)
            return render(request, 'doctor_appointments.html', {'appointments': appointments})
        appointments = Appointment.objects.filter(patient=request.user)
        return render(request, 'patient_appointments.html', {'appointments': appointments})
    return redirect('login')


@login_required
def update_appointment_status(request, appointment_id):
    """Allow doctors to update appointment status"""
    appointment = get_object_or_404(Appointment, id=appointment_id)
    doctor = Doctor.objects.filter(user=request.user).first()

    if not doctor or appointment.doctor != doctor:
        messages.error(request, 'You are not authorized to update this appointment.')
        return redirect('doctor_dashboard')

    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['confirmed', 'cancelled', 'completed']:
            appointment.status = status
            appointment.save()
            messages.success(request, {
                'confirmed': 'Appointment confirmed successfully!',
                'cancelled': 'Appointment cancelled.',
                'completed': 'Appointment marked as completed.'
            }.get(status))
        else:
            messages.error(request, 'Invalid status.')

    return redirect('doctor_dashboard')


@login_required
def cancel_appointment(request, appointment_id):
    """Allow patients to cancel their appointments"""
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

    if appointment.status in ['pending', 'confirmed']:
        appointment.status = 'cancelled'
        appointment.save()
        messages.success(request, 'Appointment cancelled successfully.')
    else:
        messages.error(request, 'Cannot cancel this appointment.')

    return redirect('patient_dashboard')
