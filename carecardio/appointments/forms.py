from django import forms
from .models import Appointment, Clincian


class AppointmentForm(forms.ModelForm):
    your_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}),
        label="Your Name",
        max_length=100,
        required=True,
    )

    your_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Phone"}),
        label="Your Phone",
        max_length=100,
        required=True,
    )

    your_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Your Email"}),
        label="Your Email",
        required=True,
    )

    your_address = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Address"}),
        label="Your Address",
        max_length=100,
        required=True,
    )

    your_schedule = forms.ChoiceField(
        choices=[
            ("", "Choose Your Schedule"),
            ("9am", "9am"),
            ("11am", "11am"),
            ("2pm", "2pm"),
            ("4pm", "4pm"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Choose Your Schedule",
        required=True,
    )

    your_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}),
        label="Choose Your Date",
        required=True,
    )

    your_message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Your Message"}),
        label="Your Message",
        max_length=1000,
        required=True,
    )

    class Meta:
        model = Appointment
        fields = ["your_name", "your_phone", "your_email",
                  "your_address", "your_schedule", "your_date", "your_message"]
