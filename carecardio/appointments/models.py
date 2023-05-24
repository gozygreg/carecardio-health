from django.db import models
from django.contrib.auth.models import User

class Clincian(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as per your requirements

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add more fields as per your requirements

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    clinician = models.ForeignKey(Clincian, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    # Add more fields as per your requirements

    def __str__(self):
        return f"{self.patient} - {self.clinician} - {self.date} {self.time}"