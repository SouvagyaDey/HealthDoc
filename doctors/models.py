from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from hospitals.models import Hospital

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('general', 'General Medicine'),
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('gynecology', 'Gynecology'),
        ('dermatology', 'Dermatology'),
        ('psychiatry', 'Psychiatry'),
        ('oncology', 'Oncology'),
        ('gastroenterology', 'Gastroenterology'),
        ('pulmonology', 'Pulmonology'),
        ('endocrinology', 'Endocrinology'),
        ('nephrology', 'Nephrology'),
        ('rheumatology', 'Rheumatology'),
        ('ophthalmology', 'Ophthalmology'),
        ('ent', 'ENT (Ear, Nose, Throat)'),
        ('anesthesiology', 'Anesthesiology'),
        ('radiology', 'Radiology'),
        ('pathology', 'Pathology'),
        ('surgery', 'General Surgery'),
        ('emergency', 'Emergency Medicine'),
    ]

    QUALIFICATION_CHOICES = [
        ('mbbs', 'MBBS'),
        ('md', 'MD'),
        ('ms', 'MS'),
        ('dm', 'DM'),
        ('mch', 'MCh'),
        ('diploma', 'Diploma'),
        ('fellowship', 'Fellowship'),
    ]

    # Basic Information
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, help_text="Doctor's login account")
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    qualification = models.CharField(max_length=100)
    
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')
    experience_years = models.PositiveIntegerField(
        default=0,
        help_text="Years of experience"
    )
    consultation_fee = models.PositiveIntegerField(
        default=500,
        help_text="Consultation fee in INR"
    )
    
    # Contact Information
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    # Availability
    available_days = models.CharField(
        max_length=100, 
        default="Monday to Friday",
        help_text="Days when doctor is available"
    )
    available_time = models.CharField(
        max_length=100, 
        default="9:00 AM - 5:00 PM",
        help_text="Time when doctor is available"
    )
    
    # Additional Information
    languages_spoken = models.CharField(
        max_length=200, 
        default="English, Hindi",
        help_text="Languages the doctor can speak"
    )
    bio = models.TextField(blank=True, null=True, help_text="Doctor's biography")
    
    # Rating and Reviews
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        default=4.0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
    
    def __str__(self):
        return f"Dr. {self.name} - {self.get_specialization_display()}"
    
    @property
    def full_qualification(self):
        """Return formatted qualification string"""
        return f"Dr. {self.name}, {self.qualification}"
    
    @property
    def consultation_fee_formatted(self):
        """Return formatted consultation fee"""
        return f"₹{self.consultation_fee}"
