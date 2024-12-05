from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
from . import forms, models
from django.contrib.auth.decorators import login_required,user_passes_test



# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

def main_page(request):
  # if request.user.is_authenticated:
  #       return HttpResponseRedirect('afterlogin')
  return render(request, 'main_page.html')

def patient_click_page(request):
  return render(request, 'patientclick.html')

def hos_staff_click_page(request):
  return render(request, 'hospitalstaffclick.html')

def admin_click_page(request):
  return render(request, 'adminclick.html')

def recep_click_page(request):
  return render(request, 'recepclick.html')

def doctor_click_page(request):
  return render(request, 'doctorclick.html')

def nurse_click_page(request):
  return render(request, 'nurseclick.html')

def about_us(request):
  return render(request, 'aboutus.html')
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('main_page')
    else:
      messages.success(request, ("The credentials you provided cannot be determined to be authentic."))
      return redirect('nurse_login')
  return render(request, 'nurselogin.html', {})

def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return redirect('patient_login')
    return render(request,'patientsignup.html',context=mydict)


#doctor
def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return redirect('doctor_login')
    return render(request,'doctorsignup.html',context=mydict)


#nurse
def nurse_signup_view(request):
    userForm=forms.NurseUserForm()
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.NurseUserForm(request.POST)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            my_nurse_group = Group.objects.get_or_create(name='NURSE')
            my_nurse_group[0].user_set.add(user)
        return redirect('nurse_login')
    return render(request,'nursesignup.html',context=mydict)

#admin
def admin_signup_view(request):
    userForm=forms.AdminUserForm()
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.AdminUserForm(request.POST)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
        return redirect('admin_login')
    return render(request,'adminsignup.html',context=mydict)

#recep
def recep_signup_view(request):
    userForm=forms.RecepUserForm()
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.RecepUserForm(request.POST)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            my_recep_group = Group.objects.get_or_create(name='RECEP')
            my_recep_group[0].user_set.add(user)
        return redirect('recep_login')
    return render(request,'recepsignup.html',context=mydict)

#-----------for checking user is doctor , patient or admin 
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()
def is_nurse(user):
    return user.groups.filter(name='NURSE').exists()
def is_recep(user):
    return user.groups.filter(name='RECEP').exists()

#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR OR PATIENT
def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        return redirect('doctor-dashboard')
    elif is_patient(request.user):
        return redirect('patient-dashboard')
    elif is_nurse(request.user):
        return redirect('nurse-dashboard')
    elif is_recep(request.user):
        return redirect('recep-dashboard')
    return HttpResponse('123')
    


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard(request):
    return render(request,'patient/dashboard.html')


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard(request):
   return render(request, 'doctor/dashboard.html')


@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_dashboard(request):
   return render(request, 'nurse/dashboard.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard(request):
   return render(request, 'adminn/dashboard.html')


@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_dashboard(request):
   return render(request, 'recep/dashboard.html')


#################################################################################
#                             for admin                                         #
#################################################################################

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_patient(request):
   patients = models.Patient.objects.all()
   return render(request, 'adminn/patient.html', {'patients':patients})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_patient(request):
    if request.method == 'POST':
        form = forms.PatientForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('admin-patient')
        else:
            return render(request, 'adminn/add_patient.html', {'form': form, 'error': 'Form data is invalid'})
    
    form = forms.PatientForm()
    return render(request, 'adminn/add_patient.html', {'form': form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_delete_patient(request, patientid):
    patient = get_object_or_404(models.Patient, patientid=patientid)
    
    # Handle POST request for deletion
    if request.method == 'POST':
        patient.delete()
        messages.success(request, f'Patient {patient.get_name} deleted successfully.')
        return redirect('admin-patient')  # Redirect to the patient list page

    return render(request, 'adminn/delete_patient.html', {'patient': patient})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_edit_patient(request, patientid):
    patient = get_object_or_404(models.Patient, patientid=patientid)

    if request.method == 'POST':
      form = forms.PatientForm(request.POST, instance=patient)
      if form.is_valid():
         form.save()
         return redirect('admin-patient')
    form = forms.PatientForm(instance=patient)
    return render(request, 'adminn/edit_patient.html', {'form':form, 'patient':patient})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_appointment(request):
   appointment = models.Appointment.objects.all()
   return render(request, 'adminn/appointment.html', {'appointment':appointment})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_delete_appointment(request, appointmentid):
   appointment = get_object_or_404(models.Appointment, appointmentid=appointmentid)
   if request.method == 'POST':
      appointment.delete()
      messages.success(request, f'Appointment {appointmentid} deleted successfully!')
      return redirect('admin-appointment')
   return render(request, 'adminn/delete_appointment.html', {'appointment':appointment})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_edit_appointment(request, appointmentid):
    appointment = get_object_or_404(models.Appointment, appointmentid=appointmentid)
    if request.method == 'POST':
      form = forms.Appointment(request.POST, instance=appointment)
      if form.is_valid():
         form.save()
         return redirect('admin-appointment')
    form = forms.Appointment(instance=appointment)
    return render(request, 'adminn/edit_appointment.html', {'form':form,'appointment':appointment})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_appointment(request):
    if request.method == 'POST':
      form = forms.Appointment(request.POST)
      if form.is_valid():
         form.save()
         return redirect('admin-appointment')
      else:
         return render(request, 'adminn/add_appointment.html', {'form':form, 'error':'Form data is not valid'})
    
    form = forms.Appointment()
    return render(request, 'adminn/add_appointment.html', {'form':form})