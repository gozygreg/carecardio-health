from django.db import models

class Appointment(models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    date_of_appointment = models.DateField()
    time_of_appointment = models.TimeField()
    symptoms = [
        ('Chest Pain', 'Chest Pain'),
        ('Palpitations', 'Palpitations'),
        ('Breathlessness', 'Breathlessness'),
        ('Feeling Dizzy', 'Feeling Dizzy'),
        ('Fatigue', 'Fatigue'),
        ('Swollen Limbs', 'Swollen Limbs'),
        ('Neck Pain', 'Neck Pain'),
        ('Jaw Pain', 'Jaw Pain'),
        ('Throat Pain', 'Throat Pain'),
        ('Upper Belly Pain', 'Upper Belly Pain'),
        ('Back Pain', 'Back Pain'),
    ]
    reason_for_appointment = models.CharField(max_length=20, choices=symptoms)
    other_symptoms = models.TextField(blank=True)
    additional_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client_name} - {self.date_of_appointment} - {self.time_of_appointment}"