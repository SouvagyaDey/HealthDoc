from django import forms
from .models import Appointment
from doctors.models import Doctor
from django.utils import timezone
from datetime import datetime, timedelta

class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        widget=forms.HiddenInput(),
        required=False
    )
    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'min': timezone.now().date()
        })
    )
    appointment_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control'
        })
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Describe your symptoms or reason for visit'
        }),
        required=False
    )

    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'appointment_time', 'reason']

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get('doctor')
        appointment_date = cleaned_data.get('appointment_date')
        appointment_time = cleaned_data.get('appointment_time')

        if doctor and appointment_date and appointment_time:
            # Check if the appointment slot is already taken
            existing_appointment = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).exists()
            
            if existing_appointment:
                raise forms.ValidationError(
                    'This time slot is already booked. Please choose another time.'
                )

        return cleaned_data
