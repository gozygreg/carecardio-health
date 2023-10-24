from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import AppointmentForm
from .models import Clincian, Appointment
from django.contrib import messages


@login_required
def schedule_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient
            appointment.save()
            form.save()
            return redirect("appointments/appointments_list")
    else:
        form = AppointmentForm()
    return render(request, "appointments/schedule_appointment.html", {"form": form})


@login_required
def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient
            appointment.save()

            appointment_info = {
                "Name": form.cleaned_data["your_name"],
                "Phone": form.cleaned_data["your_phone"],
                "Email": form.cleaned_data["your_email"],
                "Address": form.cleaned_data["your_address"],
                "Schedule": form.cleaned_data["your_schedule"],
                "Day": form.cleaned_data["your_date"],
                "Message": form.cleaned_data["your_message"],
                "Appointment Date": appointment.date,
                "Appointment Time": appointment.time,
            }

            message = "\n".join(
                [f"{key}: {value}" for key, value in appointment_info.items()])

            send_mail(
                "Appointment Request",
                message,
                form.cleaned_data["your_email"],
                ["gregmeditechinc@gmail.com"],
                fail_silently=False,
            )

            return render(request, "appointments/appointment.html", appointment_info)

    return render(request, "home/index.html")


@login_required
def available_clinician(request):
    clinicians = Clincian.objects.all()
    return render(
        request, "appointments/available_clinician.html", {
            "clinicians": clinicians}
    )
