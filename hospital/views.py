from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment
from .forms import PatientForm, DoctorForm, AppointmentForm

def home(request):
    return render(request, 'hospital/home.html')

def patients(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm()
    patients = Patient.objects.all()
    return render(request, 'hospital/patients.html', {'form': form, 'patients': patients})

def doctors(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctors.html', {'form': form, 'doctors': doctors})

def appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()
    appointments = Appointment.objects.all()
    return render(request, 'hospital/appointments.html', {'form': form, 'appointments': appointments})