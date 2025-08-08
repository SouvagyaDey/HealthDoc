from django import forms
from django.contrib.auth.models import User
from doctors.models import Doctor
from .models import Profile

class DoctorRegisterForm(forms.ModelForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        from django.contrib.auth.models import User
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken. Please choose another.')
        return username
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = Doctor
        fields = ['name', 'image', 'specialization', 'qualification', 'hospital',
                  'experience_years', 'consultation_fee', 'phone', 'email',
                  'available_days', 'available_time', 'languages_spoken', 'bio']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
        )
        profile = Profile.objects.get(user=user)
        profile.role = 'doctor'
        profile.save()

        doctor = super().save(commit=False)
        doctor.user = user
        if commit:
            doctor.save()
        return user

class PatientRegisterForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
        )
        profile = Profile.objects.get(user=user)
        profile.role = 'patient'
        profile.save()
        return user
