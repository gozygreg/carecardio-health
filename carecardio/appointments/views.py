from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Clincian, Appointment


@login_required
def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient
            appointment.save()
            return redirect('appointments:appointments_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/schedule_appointment.html', {'form': form})


@login_required
def appointments_list(request):
    appointments = Appointment.objects.filter(patient=request.user.patient)
    return render(request, 'appointments/appointments_list.html', {'appointments': appointments})


@login_required
def available_doctors(request):
    doctors = Clinician.objects.all()
    return render(request, 'appointments/available_doctors.html', {'clinician': clinician})
