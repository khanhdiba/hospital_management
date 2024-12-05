from django import forms
from django.contrib.auth.models import User
from . import models
# from django.contrib.auth.forms import UserCreationForm

class AdminUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class RecepUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class NurseUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
  class Meta:
        model = models.Patient
        fields = ['patientid', 'patientssn', 'firstname', 'midname', 'lastname', 'patientdob', 'gender', 'phonenumber', 'street', 'district', 'city']


class Appointment(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['appointmentid', 'patientid', 'doctorid', 'appointmentdate', 'appointmenttime']






