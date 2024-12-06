from django import forms
from django.contrib.auth.models import User
from . import models
from django.forms.widgets import DateInput, Select

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
    patientdob = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=Select(attrs={'class': 'form-control'}),
        required=True,  # Set to False if gender is optional
    )

    class Meta:
        model = models.Patient
        fields = ['patientid', 'patientssn', 'firstname', 'midname', 'lastname', 'patientdob', 'gender', 'phonenumber', 'street', 'district', 'city']


class Appointment(forms.ModelForm):
    appointmentdate = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    appointmenttime = forms.TimeField(
        widget=DateInput(attrs={'type': 'time', 'class': 'form-control'})
    )

    class Meta:
        model = models.Appointment
        fields = ['appointmentid', 'patientid', 'doctorid', 'appointmentdate', 'appointmenttime']

class Doctor(forms.ModelForm):
    # doctorid = forms.CharField(max_length=7)
    class Meta:
        model = models.Doctor
        fields = ['license']

class MedicalStaff(forms.ModelForm):
    staffid = forms.CharField(max_length=7, min_length=7)
    staffssn = forms.CharField(max_length=10, min_length=10)
    staffdob = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=Select(attrs={'class': 'form-control'}),
        required=True,  # Set to False if gender is optional
    )

    class Meta:
        model = models.MedicalStaff
        fields = ['staffid', 'staffssn', 'firstname', 'midname', 'lastname', 'staffdob', 'gender', 'phonenumber', 'salary', 'departmentid']


class Department(forms.ModelForm):
    departmentid = forms.ModelChoiceField(
        queryset=models.Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True  # Set to False if department is optional
    )
    class Meta:
        model = models.Department
        fields = ['departmentid', 'departmentname']

