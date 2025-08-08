from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'qualification', 'hospital', 'experience_years', 'consultation_fee', 'phone', 'email')
    search_fields = ('name', 'specialization', 'qualification', 'hospital__name')
    list_filter = ('specialization', 'hospital')
