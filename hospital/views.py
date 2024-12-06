from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
from . import forms, models
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db import transaction, IntegrityError



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
        try:
            form = forms.PatientForm(request.POST)
            if form.is_valid():
                form.save() 
                return redirect('admin-patient')
            else:
                return render(request, 'adminn/add_patient.html', {'form': form, 'error': 'Form data is invalid'})
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
    form = forms.PatientForm()
    return render(request, 'adminn/add_patient.html', {'form': form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_delete_patient(request, patientid):
    patient = get_object_or_404(models.Patient, patientid=patientid)
    
    if request.method == 'POST':
        try:
            patient.delete()
            messages.success(request, f'Patient {patient.get_name} deleted successfully.')
            return redirect('admin-patient')  # Redirect to the patient list page
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")

    return render(request, 'adminn/delete_patient.html', {'patient': patient})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_edit_patient(request, patientid):
    patient = get_object_or_404(models.Patient, patientid=patientid)

    if request.method == 'POST':
        try:
            form = forms.PatientForm(request.POST, instance=patient)
            if form.is_valid():
                form.save()
                return redirect('admin-patient')
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
        
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
        try:
            appointment.delete()
            return redirect('admin-appointment')
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
   return render(request, 'adminn/delete_appointment.html', {'appointment':appointment})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_edit_appointment(request, appointmentid):
    appointment = get_object_or_404(models.Appointment, appointmentid=appointmentid)
    if request.method == 'POST':
        try:
            form = forms.Appointment(request.POST, instance=appointment)
            if form.is_valid():
               form.save()
               return redirect('admin-appointment')
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
    form = forms.Appointment(instance=appointment)
    return render(request, 'adminn/edit_appointment.html', {'form':form,'appointment':appointment})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_appointment(request):
    if request.method == 'POST':
        try:
            form = forms.Appointment(request.POST)
            if form.is_valid():
               form.save()
               return redirect('admin-appointment')
            else:
               return render(request, 'adminn/add_appointment.html', {'form':form, 'error':'Form data is not valid'})
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
    form = forms.Appointment()
    return render(request, 'adminn/add_appointment.html', {'form':form})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_doctor(request):
    doctors = models.Doctor.objects.select_related('doctorid')  # Pre-fetch related MedicalStaff
    doctor_data = [
        {
            'doctorid': doctor.doctorid.staffid,
            'did': doctor.doctorid,
            'fullname': doctor.doctorid.fullname,  
            'ssn': doctor.doctorid.staffssn, 
            'dob':doctor.doctorid.staffdob,
            'gender' : doctor.doctorid.gender,
            'phonenumber': doctor.doctorid.phonenumber,
            'salary': doctor.doctorid.salary,
            'department': doctor.doctorid.departmentid,
            'license': doctor.license,  
        }
        for doctor in doctors
    ]
    return render(request, 'adminn/doctor.html', {'doctor_data': doctor_data})


# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_add_doctor(request):
#     if request.method == 'POST':
#       try:
#         doctor_form = forms.Doctor(request.POST)
#         staff_form = forms.MedicalStaff(request.POST)
#         if doctor_form.is_valid():
#             messages.success(request, 'doctor form correct')
#         else:
#             messages.error(request, 'doctor form incorrect')
        
#         if staff_form.is_valid():
#             messages.success(request, 'staff form correct')
#         else:
#             messages.error(request, 'staff form incorrect')
#         if doctor_form.is_valid():
#            staff_form.save()
#            doctor_form.save()
#            return redirect('admin-doctor')
#         else:
#            context = {'doctor_form':doctor_form,'staff_form':staff_form, 'error':'Input values are invalid.'}
#            return render(request, 'adminn/add_doctor.html', context)
#       except Exception as e:
#         messages.error(request, f"An unexpected error occurred: {str(e)}")
#     doctor_form = forms.Doctor()
#     staff_form = forms.MedicalStaff()
#     context = {'doctor_form':doctor_form,'staff_form':staff_form}
#     return render(request, 'adminn/add_doctor.html', context)

# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_add_doctor(request):
#     if request.method == 'POST':
#         doctor_form = forms.Doctor(request.POST)
#         staff_form = forms.MedicalStaff(request.POST)
#         de_form = forms.Department(request.POST)
#         if doctor_form.is_valid() and staff_form.is_valid() and de_form.is_valid(): 
#             try:
#                 staff_instance = staff_form.save() 
#                 doctor_form.instance.doctorid = staff_instance 
#                 doctor_form.save()
#                 messages.success(request, 'Doctor added successfully!')
#                 return redirect('admin-doctor') 
#             except Exception as e:
#                 messages.error(request, f"An unexpected error occurred: {str(e)}")
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             context = {'doctor_form': doctor_form, 'staff_form': staff_form}
#             return render(request, 'adminn/add_doctor.html', context)
#     else:
#         doctor_form = forms.Doctor()
#         staff_form = forms.MedicalStaff()
#         context = {'doctor_form': doctor_form, 'staff_form': staff_form}
#         return render(request, 'adminn/add_doctor.html', context)


# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_add_doctor(request):
    # if request.method == 'POST':
    #     doctor_form = forms.Doctor(request.POST)
    #     staff_form = forms.MedicalStaff(request.POST)
    #     de_form = forms.Department(request.POST)  # Department form with existing departments
    #     # if doctor_form.is_valid():
        #     messages.success(request, 'doctor form correct')
        # else:
        #     messages.error(request, 'doctor form incorrect')
        
        # if staff_form.is_valid():
        #     messages.success(request, 'staff form correct')
        # else:
        #     messages.error(request, 'staff form incorrect')

        # if de_form.is_valid():
        #     messages.success(request, 'department form correct')
        # else:
        #     messages.error(request, 'department form incorrect')


    #     if doctor_form.is_valid() and staff_form.is_valid() and de_form.is_valid():
    #         try:
    #             # Save the MedicalStaff instance and associate it with the selected department
    #             staff_instance = staff_form.save(commit=False)
    #             staff_instance.departmentid = de_form.cleaned_data['departmentid']  # Link to selected department
    #             staff_instance.save()

    #             # Save the Doctor instance and link it to the MedicalStaff instance
    #             doctor_instance = doctor_form.save(commit=False)
    #             doctor_instance.doctorid = staff_instance  # Link MedicalStaff to Doctor
    #             doctor_instance.save()

    #             # Success message
    #             messages.success(request, 'Doctor added successfully!')
    #             return redirect('admin-doctor')

    #         except Exception as e:
    #             # Error message for any unexpected errors
    #             messages.error(request, f"An unexpected error occurred: {str(e)}")

    #     else:
    #         # Error message for invalid forms
    #         messages.error(request, 'Please correct the errors below.')

    # else:
    #     # Initialize empty forms for a GET request
    #     doctor_form = forms.Doctor()
    #     staff_form = forms.MedicalStaff()
    #     de_form = forms.Department()

    # # Render the form context
    # context = {
    #     'doctor_form': doctor_form,
    #     'staff_form': staff_form,
    #     'de_form': de_form,  # Add Department form to context
    #         'staff_form_errors': staff_form.errors,  # Pass errors to template
    # 'de_form_errors': de_form.errors,  # Pass errors to template
    # }
    # return render(request, 'adminn/add_doctor.html', context)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_doctor(request):
    if request.method == 'POST':
        doctor_form = forms.Doctor(request.POST)
        staff_form = forms.MedicalStaff(request.POST)
        if doctor_form.is_valid() and staff_form.is_valid():
            staff_instance = staff_form.save()  # Save MedicalStaff instance
            doctor_instance = doctor_form.save(commit=False)  # Don't save yet
            doctor_instance.doctorid = staff_instance  # Set doctorid to the saved MedicalStaff instance
            doctor_instance.save()  # Save the Doctor instance
            messages.success(request, 'Doctor added successfully!')
            return redirect('admin-doctor')
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'adminn/add_doctor.html', {'doctor_form': doctor_form, 'staff_form': staff_form})
    else:
        doctor_form = forms.Doctor()
        staff_form = forms.MedicalStaff()
        return render(request, 'adminn/add_doctor.html', {'doctor_form': doctor_form, 'staff_form': staff_form})
    

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_delete_staff(request, staffid):
   staff = get_object_or_404(models.MedicalStaff, staffid = staffid)
   if request.method == 'POST':
        try:
            staff.delete()
            return redirect('admin-doctor')
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
   return render(request, 'adminn/delete_staff.html', {'staff':staff})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_edit_doctor(request, doctorid):
    # Get the Doctor instance (and associated MedicalStaff instance) based on the doctorid
    doctor_instance = get_object_or_404(models.Doctor, doctorid=doctorid)
    staff_instance = doctor_instance.doctorid  # Access the associated MedicalStaff instance
    
    if request.method == 'POST':
        # Initialize the forms with the existing data
        doctor_form = forms.Doctor(request.POST, instance=doctor_instance)
        staff_form = forms.MedicalStaff(request.POST, instance=staff_instance)
        
        if doctor_form.is_valid() and staff_form.is_valid():
            try:
                # Save both forms (the MedicalStaff and Doctor models)
                staff_instance = staff_form.save()  # Save MedicalStaff instance first
                doctor_instance = doctor_form.save(commit=False)  # Save Doctor instance
                doctor_instance.doctorid = staff_instance  # Link updated MedicalStaff instance
                doctor_instance.save()  # Save the updated Doctor instance
                
                messages.success(request, 'Doctor updated successfully!')
                return redirect('admin-doctor')  # Redirect to the list of doctors (or any other page)
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
        else:
            messages.error(request, 'Please correct the errors below.')
    
    else:
        # Initialize the forms with the existing data
        doctor_form = forms.Doctor(instance=doctor_instance)
        staff_form = forms.MedicalStaff(instance=staff_instance)
    
    # Pass the forms to the template for rendering
    return render(request, 'adminn/edit_doctor.html', {
        'doctor_form': doctor_form,
        'staff_form': staff_form,
        'doctor_instance': doctor_instance
    })



#################################################################################
#                             for doctor                                        #
#################################################################################


#################################################################################
#                             for nurse                                         #
#################################################################################


#################################################################################
#                             for patient                                       #
#################################################################################


#################################################################################
#                             for recep                                         #
#################################################################################

@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_admit(request):
   patients = models.Patient.objects.all()
   return render(request, 'recep/patient.html', {'patients':patients})


@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_add_patient(request):
    if request.method == 'POST':
        form = forms.PatientForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('recep-patient')
        else:
            return render(request, 'recep/add_patient.html', {'form': form, 'error': 'Form data is invalid'})
    
    form = forms.PatientForm()
    return render(request, 'recep/add_patient.html', {'form': form})

@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_delete_patient(request, patientid):
    patient = get_object_or_404(models.Patient, patientid=patientid)
    
    # Handle POST request for deletion
    if request.method == 'POST':
        patient.delete()
        messages.success(request, f'Patient {patient.get_name} deleted successfully.')
        return redirect('recep-patient')  # Redirect to the patient list page

    return render(request, 'recep/delete_patient.html', {'patient': patient})


@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_edit_patient(request, patientid):
    patient = get_object_or_404(models.Patient, patientid=patientid)

    if request.method == 'POST':
      form = forms.PatientForm(request.POST, instance=patient)
      if form.is_valid():
         form.save()
         return redirect('recep-patient')
    form = forms.PatientForm(instance=patient)
    return render(request, 'recep/edit_patient.html', {'form':form, 'patient':patient})


@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_appointment(request):
   appointment = models.Appointment.objects.all()
   return render(request, 'recep/appointment.html', {'appointment':appointment})

@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_delete_appointment(request, appointmentid):
   appointment = get_object_or_404(models.Appointment, appointmentid=appointmentid)
   if request.method == 'POST':
      appointment.delete()
      messages.success(request, f'Appointment {appointmentid} deleted successfully!')
      return redirect('recep-appointment')
   return render(request, 'recep/delete_appointment.html', {'appointment':appointment})


@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_edit_appointment(request, appointmentid):
    appointment = get_object_or_404(models.Appointment, appointmentid=appointmentid)
    if request.method == 'POST':
      form = forms.Appointment(request.POST, instance=appointment)
      if form.is_valid():
         form.save()
         return redirect('recep-appointment')
    form = forms.Appointment(instance=appointment)
    return render(request, 'recep/edit_appointment.html', {'form':form,'appointment':appointment})

@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_add_appointment(request):
    if request.method == 'POST':
      form = forms.Appointment(request.POST)
      if form.is_valid():
         form.save()
         return redirect('recep-appointment')
      else:
         return render(request, 'recep/add_appointment.html', {'form':form, 'error':'Form data is not valid'})
    
    form = forms.Appointment()
    return render(request, 'recep/add_appointment.html', {'form':form})
