from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):

    Role_Choices = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=Role_Choices)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"