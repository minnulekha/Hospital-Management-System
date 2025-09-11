from django.db import models
from django.contrib.auth.models import AbstractUser

class MYUSER(AbstractUser):
    user_type = models.CharField(max_length=10)

class Doctor(models.Model):
    DEPARTMENT_CHOICES = [
        ("General", "General"),   
        ("Cardiology", "Cardiology"),
        ("Neurology", "Neurology"),
        ("ENT", "ENT"),
        ("Orthopedics", "Orthopedics"),
        ("Pediatrics", "Pediatrics"),
        ("Dermatology", "Dermatology"),
    ]

    Doctor_id = models.ForeignKey(MYUSER, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    doc_image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default="General")  # ✅ default set to General

    def __str__(self):
        return f"{self.name} ({self.department})"


class Patient(models.Model):
    Patient_id = models.ForeignKey(MYUSER, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    admitted_on = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)  # NEW FIELD

    def __str__(self):
        return self.name

    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField()
    time = models.TimeField()
    symptoms = models.TextField(blank=True, null=True)   # NEW FIELD

    def __str__(self):
        return f"{self.patient} - {self.doctor} ({self.date} {self.time})"

    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.subject