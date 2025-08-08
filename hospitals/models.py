from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Hospital(models.Model):
    # Basic Information
    image = models.ImageField(upload_to='hospital_images/', blank=True, null=True)
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    
    # Contact Information
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    # Hospital Details
    bed_count = models.PositiveIntegerField(
        default=0,
        help_text="Total number of beds available"
    )
    established_year = models.PositiveIntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(1800), MaxValueValidator(timezone.now().year)],
        help_text="Year the hospital was established"
    )
    accreditation = models.CharField(
        max_length=200, 
        blank=True, null=True,
        help_text="Accreditation details (e.g., NABH, JCI, ISO)"
    )
    
    # Services Available (Boolean fields)
    emergency_services = models.BooleanField(default=False)
    ambulance_service = models.BooleanField(default=False)
    blood_bank = models.BooleanField(default=False)
    pharmacy = models.BooleanField(default=False)
    cafeteria = models.BooleanField(default=False)
    parking_available = models.BooleanField(default=False)

class HospitalReview(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating out of 5"
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} - {self.hospital.name} - {self.rating}/5"