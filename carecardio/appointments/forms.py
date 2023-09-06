from django import forms
from .models import Appointment, Clincian


# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ["clinician", "date", "time"]


class AppointmentForm(forms.ModelForm):
    your_clinician = forms.ModelChoiceField(
        queryset=Clincian.objects.all(),
        label="Choose Your Clinician",
        empty_label="Choose Your Clinician",
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        model = Appointment
        fields = ["your_clinician", "date", "time"]
