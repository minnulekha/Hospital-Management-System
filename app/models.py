from django.db import models
from django.contrib.auth.models import AbstractUser

class MYUSER(AbstractUser):
    user_type = models.CharField(max_length=10)

class Doctor(models.Model):
    Doctor_id = models.ForeignKey(MYUSER, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    doc_image = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def _str_(self):
        return self.name

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

    def _str_(self):
        return str(self.patient)
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.subject