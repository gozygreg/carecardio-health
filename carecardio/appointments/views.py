from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import AppointmentForm
from .models import Clincian, Appointment


# @login_required
def schedule_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # appointment = form.save(commit=False)
            # appointment.patient = request.user.patient
            # appointment.save()
            form.save()
            return redirect("appointments/appointments_list")
    else:
        form = AppointmentForm()
    return render(request, "appointments/schedule_appointment.html", {"form": form})


# @login_required
def appointment(request):
    if request.method == "POST":
        your_name = request.POST["your-name"]
        your_email = request.POST["your-email"]
        your_phone = request.POST["your-phone"]
        your_address = request.POST["your-address"]
        your_schedule = request.POST["your-schedule"]
        your_date = request.POST["your-date"]
        your_message = request.POST["your-message"]

        # send an email
        appointment = (
            "Name: "
            + your_name
            + " Phone: "
            + your_phone
            + " Email: "
            + your_email
            + " Address: "
            + your_address
            + " Schedule: "
            + your_schedule
            + "Day : "
            + your_date
            + "Message: "
            + your_message
        )

        send_mail(
            "Appointment Request",
            appointment,  # message
            your_email,  # from email
            ["gregmeditechinc@gmail.com"],  # to email
        )

        return render(
            request,
            "appointments/appointment.html",
            {
                "your_name": your_name,
                "your_phone": your_phone,
                "your_email": your_email,
                "your_address": your_address,
                "your_schedule": your_schedule,
                "your_date": your_date,
                "your_message": your_message,
            },
        )

    else:
        return render(request, "home/index.html")


# @login_required
def available_clinician(request):
    doctors = Clinician.objects.all()
    return render(
        request, "appointments/available_clinician.html", {"clinician": clinician}
    )
