from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Clincian, Appointment


# @login_required
def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # appointment = form.save(commit=False)
            # appointment.patient = request.user.patient
            # appointment.save()
            form.save()
            return redirect('appointments/appointments_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/schedule_appointment.html', {'form': form})


# @login_required
def appointment(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send email
        send_email(
            message_name,
            message,
            message_email,
            ['goziennabuife@yahoo.com'],
        )

        return render(request, 'appointment.html', {})

    else:
        return render(request, 'home.html')


# @login_required
def available_clinician(request):
    doctors = Clinician.objects.all()
    return render(request, 'appointments/available_clinician.html', {'clinician': clinician})
