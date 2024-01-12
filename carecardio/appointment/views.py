from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm


@staff_member_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment/appointment_list.html', {'appointments': appointments})

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/create_appointment.html', {'form': form})