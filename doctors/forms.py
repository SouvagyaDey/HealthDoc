from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'user', 'name', 'image', 'specialization', 'qualification', 'hospital', 'experience_years',
            'consultation_fee', 'phone', 'email', 'available_days', 'available_time', 'languages_spoken', 'bio', 'rating'
        ]
        widgets = {
            'available_days': forms.CheckboxSelectMultiple(),
            'available_time': forms.TimeInput(attrs={'type': 'time'}),
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
