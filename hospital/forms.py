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
        fields=['username','password']
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
        fields=['username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets = {
        'password': forms.PasswordInput(),
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

class Manages(forms.ModelForm):
    class Meta:
        model = models.Manages
        fields = ['startdate']

class Nurse(forms.ModelForm):
    class Meta:
        model = models.Nurse
        fields = ['yearexperience']

class MedicalRecord(forms.ModelForm):
    recorddate= forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    class Meta:
        model = models.MedicalRecord
        fields = ['recordid', 'patientid', 'recorddate', 'diagnosis', 'testresult']
        labels = {
            'recordid': 'Record ID',
            'patientid': 'Patient ID',
            'recorddate': 'Date of Record',
            'diagnosis': 'Diagnosis',
            'testresult': 'Test Results',
        }
        widgets = {
            'recordid': forms.TextInput(attrs={'class': 'form-control'}),
            'patientid': forms.TextInput(attrs={'class': 'form-control'}),
            'diagnosis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'testresult': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
class Treatment(forms.ModelForm):
    treatmentdate = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    class Meta:
        model = models.Treatment
        fields = ['patientid','treatmentid', 'treatmentdate', 'treatmentprocedure']
        labels = {
            'patientid': 'Patient ID',
            'treatmentid': 'Treatment ID',
            'treatmentdate': 'Date of Treatment',
            'treatmentprocedure': 'Procedure',
        }
        widgets = {
            'patientid': forms.TextInput(attrs={'class': 'form-control'}),
            'treatmentid': forms.TextInput(attrs={'class': 'form-control'}),
            'treatmentprocedure': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# class Room(forms.ModelForm):
#     class Meta:
#         model = models.Room
#         fields = ['roomid', 'capacity']
#         labels = {
#             'roomid': 'Room ID',
#         }
#         widgets = {
#             'roomid':forms.ModelChoiceField(
#                 queryset=models.Room.objects.all(),
#                 widget=Select(attrs={'class': 'form-control'}),
#                 required=True
#             ),
#             # 'roomid':forms.Select(attrs={'class': 'form-control'}),
#         }

# class TakesCare(forms.ModelForm):
#     class Meta:
#         model = models.TakesCare
#         fields = ['roomid', 'nurseid']


# class AdmittedTo(forms.ModelForm):
#     class Meta:
#         model = models.AdmittedTo
#         fields = ['patientid', 'roomid', 'admitteddate', 'dischargeddate']

class AddRoom(forms.Form):
    # ROOM_CHOICES = [(str(i), str(i)) for i in range(101, 111)]
    # roomid = forms.ChoiceField(
    #     choices=ROOM_CHOICES,
    #     widget=forms.Select(attrs={'class':'form-control'}),
    #     label='Room ID',
    #     required=True,
    # )

    patientid = forms.ModelChoiceField(
        queryset=models.Patient.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Patient ID'
    )

    nurseid = forms.ModelChoiceField(
        queryset=models.Nurse.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Nurse ID'
    )

    admitted = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Admitted Date'
    )

    discharged = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Discharged Date'
    )
    # class Meta:
    #     fields = ['roomid', 'patientid', 'nurseid', 'admitted', 'discharged']

class PatientAppointment(forms.Form):

    doctorid = forms.ModelChoiceField(
        queryset=models.Doctor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Doctor ID'
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Appointment Date'
    )

    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type' : 'time', 'class' : 'form-control'}),
        label='Appointment Time'
    )

