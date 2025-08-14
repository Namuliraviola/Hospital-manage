from django.db import models
from django.utils import timezone

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True, blank=True)
    address = models.TextField(blank=True)
    medical_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['last_name', 'first_name']

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('GP', 'General Practitioner'),
        ('CARD', 'Cardiologist'),
        ('DERM', 'Dermatologist'),
        ('PEDS', 'Pediatrician'),
        ('ORTH', 'Orthopedist'),
        ('NEUR', 'Neurologist'),
        ('OTHER', 'Other'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=5, choices=SPECIALIZATION_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"
    
    class Meta:
        ordering = ['last_name', 'first_name']

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('SCH', 'Scheduled'),
        ('COM', 'Completed'),
        ('CAN', 'Cancelled'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField(default=timezone.now)
    appointment_time = models.TimeField()
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='SCH')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.appointment_date}"
    
    class Meta:
        ordering = ['-appointment_date', '-appointment_time']
        unique_together = ['doctor', 'appointment_date', 'appointment_time']