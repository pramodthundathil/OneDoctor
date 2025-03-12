from django.db import models

# Create your models here.

class Doctor_consultation(models.Model):
    
    Patiant_name = models.CharField(max_length=200)
    Patiant_disease = models.CharField(max_length=200)
    Doctor_name = models.CharField(max_length=200)
    appoiment_time = models.TimeField(auto_now_add=False)
    appointment_date = models.DateField(auto_now_add=False)
    
class DoctorAdd(models.Model):
    
    Doctor_name = models.CharField(max_length=200)
    SPECIALIZATION_CHOICES = [
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Neurologist', 'Neurologist'),
        ('Pediatrician', 'Pediatrician'),
        ('General', 'General'),
        ('Orthopedic', 'Orthopedic'),
        ('Psychiatrist', 'Psychiatrist'),
        ('Oncologist', 'Oncologist'),
        ('Gynecologist', 'Gynecologist'),
        ('Urologist', 'Urologist'),
    ]
    Doctor_spacial = models.CharField(max_length=200, choices=SPECIALIZATION_CHOICES)
    Date_joined = models.DateField(auto_now=False)
    
