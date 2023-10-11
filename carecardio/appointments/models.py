from django.db import models
from django.contrib.auth.models import User



class Clincian(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    email = models.EmailField(default=None)
    # Add more fields as per your requirements

    def __str__(self):
        return self.name

  
class Patient(models.Model):
    name = models.CharField(max_length=100, default=None)
    # Add more fields as per your requirements

    def __str__(self):
        return self.name


class Appointment(models.Model):
    clinician = models.ForeignKey(Clincian, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    year = models.IntegerField(default=0)  # New field for the year
    # Add more fields as per your requirements

    def save(self, *args, **kwargs):
        # Automatically set the year to the present year
        self.year = self.date.year
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient} - {self.clinician} - {self.date} {self.time}"
