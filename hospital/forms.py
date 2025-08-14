from django import forms
from .models import Patient, Doctor, Appointment
from django.utils import timezone

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email', 'address', 'medical_history']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(),
            'medical_history': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        if dob > timezone.now().date():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return dob

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialization', 'phone_number', 'email', 'is_available']
        widgets = {
            'specialization': forms.Select(),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'appointment_time', 'status', 'notes']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
            'status': forms.Select(),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean_appointment_date(self):
        date = self.cleaned_data['appointment_date']
        if date < timezone.now().date():
            raise forms.ValidationError("Appointment date cannot be in the past.")
        return date
    
    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get('doctor')
        date = cleaned_data.get('appointment_date')
        time = cleaned_data.get('appointment_time')
        
        if doctor and date and time:
            if Appointment.objects.filter(doctor=doctor, appointment_date=date, appointment_time=time).exists():
                raise forms.ValidationError("This doctor already has an appointment at this date and time.")
        return cleaned_data