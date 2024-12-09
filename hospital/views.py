from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
from . import forms, models
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db import transaction, IntegrityError, connection



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
            # messages.success(request, f'Patient {patient.get_name} deleted successfully.')
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
            # messages.success(request, 'Doctor added successfully!')
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
def admin_delete_doctor(request, staffid):
   staff = get_object_or_404(models.MedicalStaff, staffid = staffid)
   if request.method == 'POST':
        try:
            staff.delete()
            return redirect('admin-doctor')
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
   return render(request, 'adminn/delete_doctor.html', {'staff':staff})


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
                
                # messages.success(request, 'Doctor updated successfully!')
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


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_nurse(request):
    nurses = models.Nurse.objects.select_related('nurseid')  # Pre-fetch related MedicalStaff
    nurse_data = [
        {
            'nurseid': nurse.nurseid.staffid,
            'fullname': nurse.nurseid.fullname,  
            'ssn': nurse.nurseid.staffssn, 
            'dob':nurse.nurseid.staffdob,
            'gender' : nurse.nurseid.gender,
            'phonenumber': nurse.nurseid.phonenumber,
            'salary': nurse.nurseid.salary,
            'department': nurse.nurseid.departmentid,
            'yearexperience': nurse.yearexperience,  
        }
        for nurse in nurses
    ]
    return render(request, 'adminn/nurse.html', {'nurse_data': nurse_data})



###CHECK AGAIN####
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_nurse(request):
    if request.method == 'POST':
        nurse_form = forms.Nurse(request.POST)
        staff_form = forms.MedicalStaff(request.POST)
        if nurse_form.is_valid() and staff_form.is_valid():
            staff_instance = staff_form.save() 
            nurse_instance = nurse_form.save(commit=False) 
            nurse_instance.nurseid = staff_instance  
            nurse_instance.save() 
            # messages.success(request, 'Nurse added successfully!')
            return redirect('admin-nurse')
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'adminn/add_nurse.html', {'nurse_form': nurse_form, 'staff_form': staff_form})
    else:
        nurse_form = forms.Nurse()
        staff_form = forms.MedicalStaff()
        return render(request, 'adminn/add_nurse.html', {'nurse_form': nurse_form, 'staff_form': staff_form})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_delete_nurse(request, staffid):
   staff = get_object_or_404(models.MedicalStaff, staffid = staffid)
   if request.method == 'POST':
        try:
            staff.delete()
            return redirect('admin-nurse')
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
   return render(request, 'adminn/delete_nurse.html', {'staff':staff})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_edit_nurse(request, nurseid):
    nurse_instance = get_object_or_404(models.Nurse, nurseid=nurseid)
    staff_instance = nurse_instance.nurseid 
    
    if request.method == 'POST':
        nurse_form = forms.Nurse(request.POST, instance=nurse_instance)
        staff_form = forms.MedicalStaff(request.POST, instance=staff_instance)
        
        if nurse_form.is_valid() and staff_form.is_valid():
            try:
                staff_instance = staff_form.save() 
                nurse_instance = nurse_form.save(commit=False)
                nurse_instance.nurseid = staff_instance
                nurse_instance.save()
                
                return redirect('admin-nurse')
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
        else:
            messages.error(request, 'Please correct the errors below.')
    
    else:
        nurse_form = forms.Nurse(instance=nurse_instance)
        staff_form = forms.MedicalStaff(instance=staff_instance)
    
    return render(request, 'adminn/edit_nurse.html', {
        'nurse_form': nurse_form,
        'staff_form': staff_form,
        'nurse_instance': nurse_instance
    })



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_department(request):
    q = """
            SELECT 
                d.departmentid,
                d.departmentname,
                CONCAT(ms.firstname, ' ', ms.midname, ' ', ms.lastname),
                CONCAT(m.startdate, ' - Present')
            FROM manages m
            JOIN department d ON m.departmentid = d.departmentid
            JOIN medical_staff ms ON doctorid = staffid;
            """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()
    manage_data = [
    {
        'id': row[0],
        'name': row[1],
        'headname': row[2],
        'period': row[3]
    }
    for row in rows
    ]
    return render(request, 'adminn/department.html', {'manage_data':manage_data})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_medical_record(request):
    q = """
        select recordid, m.patientid, CONCAT(p.firstname, ' ', p.midname, ' ', p.lastname), recorddate, m.treatmentid, diagnosis, testresult,
        t.treatmentdate, t.treatmentprocedure
        from medical_record m
        join patient p
        on m.patientid = p.patientid
        join treatment t on m.treatmentid = t.treatmentid
        """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()

    medical_record = [
        {
            'recordid':row[0],
            'patientid':row[1],
            'fullname':row[2],
            'date1':row[3],
            'treatmentid':row[4],
            'diagnosis':row[5],
            'result':row[6],
            'date2':row[7],
            'procedure':row[8]
        }for row in rows
    ]

    return render(request, 'adminn/medical_record.html', {'medical_record':medical_record})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_medical_record(request):
    if request.method == 'POST':
        try:
            med_form = forms.MedicalRecord(request.POST)
            treat_form = forms.Treatment(request.POST)
            if med_form.is_valid() and treat_form.is_valid():
                treat_instance = treat_form.save()
                med_instance = med_form.save(commit=False)
                med_instance.treatmentid = treat_instance
                med_instance.save()
                return redirect('admin-medical-record')
                         
            else:
                return render(request, 'adminn/add_medical_record.html', {'error':'Form is invalid'})
            

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
    med_form = forms.MedicalRecord()
    treat_form = forms.Treatment()
    context = {'med_form':med_form, 'treat_form':treat_form}

    return render(request, 'adminn/add_medical_record.html', context)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_edit_medical_record(request, recordid):
        medical_record = get_object_or_404(models.MedicalRecord, recordid=recordid)
        treatment = medical_record.treatmentid

        if request.method == 'POST':
            med_form = forms.MedicalRecord(request.POST, instance=medical_record)
            treat_form = forms.Treatment(request.POST, instance=treatment)

            if med_form.is_valid() and treat_form.is_valid():
                treat_instance = treat_form.save()

                med_instance = med_form.save(commit=False)
                med_instance.treatmentid = treat_instance
                med_instance.save()

                # messages.success(request, 'Medical record updated successfully!')
                return redirect('admin-medical-record')
            else:
                messages.error(request, 'Form validation failed. Please correct the errors.')

        else:
            med_form = forms.MedicalRecord(instance=medical_record)
            treat_form = forms.Treatment(instance=treatment)

        context = {'med_form': med_form, 'treat_form': treat_form}
        return render(request, 'adminn/edit_medical_record.html', context)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_delete_medical_record(request, recordid):
    treatment = get_object_or_404(models.Treatment, treatmentid=recordid)
    medical_record = get_object_or_404(models.MedicalRecord, recordid=recordid)
    if request.method == 'POST':
        try:
            treatment.delete()
            medical_record.delete()
            return redirect('admin-medical-record')
        except Exception as e:
            messages.error(request, f'An unexpected error occurred: {str(e)}')
    context = {'medical_record':medical_record, 'treatment':treatment}
    return render(request, 'adminn/delete_medical_record.html', context)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_room(request):
    q = """
            select roomid, capacity, roomtype, GetPatientCountAtRoom(roomid)
            from room
        """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()

    room_data=[
        {
            'roomid':row[0],
            'capacity':row[1],
            'type':row[2],
            'count':row[3]
        }for row in rows
    ]
    return render(request, 'adminn/room.html' ,{'rooms':room_data})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_room(request, roomid):
    if request.method == 'POST':
        room_form = forms.AddRoom(request.POST)
        if room_form.is_valid():
            try: 
                # q = f"""
                #         INSERT INTO admitted_to VALUES ({room_form.patientid}, {room_form.roomid}, {room_form.admitted}, {room_form.discharged});
                #         INSERT INTO takes_care (nurseID, roomID) VALUES ({room_form.nurseid}, {room_form.roomid})
                #     """
                # with connection.cursor() as cursor:
                #     cursor.execute(q)
                # roomid = room_form.cleaned_data['roomid']
                patientid = room_form.cleaned_data['patientid']
                nurseid = room_form.cleaned_data['nurseid']
                admitted = room_form.cleaned_data['admitted']
                discharged = room_form.cleaned_data['discharged']

                q = """
                    INSERT INTO admitted_to (patientid, roomid, admitteddate, dischargeddate)
                    VALUES (%s, %s, %s, %s);
                    
                    INSERT INTO takes_care (nurseid, roomid)
                    VALUES (%s, %s);
                """

                with connection.cursor() as cursor:
                    # Executing the query with parameterized values
                    cursor.execute(q, [patientid, roomid, admitted, discharged, nurseid, roomid])

                return redirect('admin-room')
            except Exception as e:
                messages.error(request, f'An unexpected error occurred: {str(e)}')
        else:
            return render(request, 'adminn/add_room.html', {'error':'Form is invalid'})
    
    room_form = forms.AddRoom()
    return render(request, 'adminn/add_room.html', {'room_form':room_form, 'roomid':roomid})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_show_room(request, roomid):
    q = """
            select p.patientid, concat(p.firstname, ' ', p.midname, ' ', p.lastname), 
            p.patientssn, p.patientdob, p.phonenumber, p.gender, concat(p.street, ' ', p.district, ' ', p.city),
            admitteddate, dischargeddate
            from patient p
            join admitted_to at on p.patientid = at.patientid
            where admitteddate <= now() and (dischargedDate > NOW() OR dischargedDate IS NULL) and at.roomid = %s
        """
    with connection.cursor() as cursor:
        cursor.execute(q, [roomid])
        rows = cursor.fetchall()
    room_info = [
        {
            'id':row[0],
            'fullname':row[1],
            'ssn':row[2],
            'dob':row[3],
            'phonenumber':row[4],
            'sex':row[5],
            'adr':row[6],
            'admitted':row[7],
            'discharged':row[8],
        }for row in rows
    ]
    return render(request, 'adminn/show_room.html', {'room_info':room_info, 'roomid':roomid})







#################################################################################
#                             for recep                                         #
#################################################################################

@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_patient(request):
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


@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_doctor(request):
    doctors = models.Doctor.objects.select_related('doctorid')  # Pre-fetch related MedicalStaff
    doctor_data = [
        {
            'doctorid': doctor.doctorid.staffid,
            'fullname': doctor.doctorid.fullname,  
            'dob':doctor.doctorid.staffdob,
            'gender' : doctor.doctorid.gender,
            'phonenumber': doctor.doctorid.phonenumber,
            'department': doctor.doctorid.departmentid,
            'license': doctor.license,  
        }
        for doctor in doctors
    ]
    return render(request, 'recep/doctor.html', {'doctor_data': doctor_data})


@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_nurse(request):
    nurses = models.Nurse.objects.select_related('nurseid')  # Pre-fetch related MedicalStaff
    nurse_data = [
        {
            'nurseid': nurse.nurseid.staffid,
            'fullname': nurse.nurseid.fullname,  
            'dob':nurse.nurseid.staffdob,
            'gender' : nurse.nurseid.gender,
            'phonenumber': nurse.nurseid.phonenumber,
            'department': nurse.nurseid.departmentid,
            'yearexperience': nurse.yearexperience,  
        }
        for nurse in nurses
    ]
    return render(request, 'recep/nurse.html', {'nurse_data': nurse_data})

@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_department(request):
    q = """
            SELECT 
                d.departmentid,
                d.departmentname,
                CONCAT(ms.firstname, ' ', ms.midname, ' ', ms.lastname),
                CONCAT(m.startdate, ' - Present')
            FROM manages m
            JOIN department d ON m.departmentid = d.departmentid
            JOIN medical_staff ms ON doctorid = staffid;
            """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()
    manage_data = [
    {
        'id': row[0],
        'name': row[1],
        'headname': row[2],
        'period': row[3]
    }
    for row in rows
    ]
    return render(request, 'recep/department.html', {'manage_data':manage_data})



@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_room(request):
    q = """
            select roomid, capacity, roomtype, GetPatientCountAtRoom(roomid)
            from room
        """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()

    room_data=[
        {
            'roomid':row[0],
            'capacity':row[1],
            'type':row[2],
            'count':row[3]
        }for row in rows
    ]
    return render(request, 'recep/room.html' ,{'rooms':room_data})


@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_add_room(request, roomid):
    if request.method == 'POST':
        room_form = forms.AddRoom(request.POST)
        if room_form.is_valid():
            try: 
                patientid = room_form.cleaned_data['patientid']
                nurseid = room_form.cleaned_data['nurseid']
                admitted = room_form.cleaned_data['admitted']
                discharged = room_form.cleaned_data['discharged']

                q = """
                    INSERT INTO admitted_to (patientid, roomid, admitteddate, dischargeddate)
                    VALUES (%s, %s, %s, %s);
                    
                    INSERT INTO takes_care (nurseid, roomid)
                    VALUES (%s, %s);
                """

                with connection.cursor() as cursor:
                    # Executing the query with parameterized values
                    cursor.execute(q, [patientid, roomid, admitted, discharged, nurseid, roomid])

                return redirect('recep-room')
            except Exception as e:
                messages.error(request, f'An unexpected error occurred: {str(e)}')
        else:
            return render(request, 'recep/add_room.html', {'error':'Form is invalid'})
    
    room_form = forms.AddRoom()
    return render(request, 'recep/add_room.html', {'room_form':room_form, 'roomid':roomid})


@login_required(login_url='receplogin')
@user_passes_test(is_recep)
def recep_show_room(request, roomid):
    q = """
            select p.patientid, concat(p.firstname, ' ', p.midname, ' ', p.lastname), 
            p.patientssn, p.patientdob, p.phonenumber, p.gender, concat(p.street, ' ', p.district, ' ', p.city),
            admitteddate, dischargeddate
            from patient p
            join admitted_to at on p.patientid = at.patientid
            where admitteddate <= now() and (dischargedDate > NOW() OR dischargedDate IS NULL) and at.roomid = %s
        """
    with connection.cursor() as cursor:
        cursor.execute(q, [roomid])
        rows = cursor.fetchall()
    room_info = [
        {
            'id':row[0],
            'fullname':row[1],
            'ssn':row[2],
            'dob':row[3],
            'phonenumber':row[4],
            'sex':row[5],
            'adr':row[6],
            'admitted':row[7],
            'discharged':row[8],
        }for row in rows
    ]
    return render(request, 'recep/show_room.html', {'room_info':room_info, 'roomid':roomid})
#################################################################################
#                             for patient                                       #
#################################################################################


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_info(request):
    patient = get_object_or_404(models.Patient, patientid=request.user.username)
    return render(request, 'patient/info.html', {'form': patient})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_health(request):
    record = models.MedicalRecord.objects.filter(patientid=request.user.username)
    treatment = models.Treatment.objects.filter(patientid=request.user.username)
    return render(request, 'patient/health.html', {'records':record, 'treatments':treatment})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_appointment(request):
    appointment = models.Appointment.objects.filter(patientid=request.user.username)
    return render(request, 'patient/appointment.html', {'appointment':appointment})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_add_appointment(request):
    if request.method == 'POST':
        try:
            form = forms.PatientAppointment(request.POST)
            if form.is_valid():
                patientid = request.user.username
                doctorid = form.cleaned_data['doctorid']
                date = form.cleaned_data['date']
                time = form.cleaned_data['time']

                # Fetch the next appointment ID
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COALESCE(MAX(appointmentid), 0) + 1 FROM appointment")
                    next_appointment_id = cursor.fetchone()[0]

                # Insert the new appointment
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO appointment (appointmentid, patientid, doctorid, appointmentdate, appointmenttime)
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        [next_appointment_id, patientid, doctorid, date, time]
                    )

                # messages.success(request, "Appointment added successfully!")
                return redirect('patient-appointment')
            else:
                return render(request, 'patient/add_appointment.html', {'form': form, 'error': 'Form data is not valid'})
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
    else:
        form = forms.PatientAppointment()
    return render(request, 'patient/add_appointment.html', {'form': form})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_room(request):
    rooms = models.AdmittedTo.objects.filter(patientid=request.user.username)
    return render(request, 'patient/room.html', {'rooms':rooms})

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_doctor(request):
    doctors = models.Doctor.objects.select_related('doctorid')  # Pre-fetch related MedicalStaff
    doctor_data = [
        {
            'doctorid': doctor.doctorid.staffid,
            'fullname': doctor.doctorid.fullname,  
            'dob':doctor.doctorid.staffdob,
            'gender' : doctor.doctorid.gender,
            'phonenumber': doctor.doctorid.phonenumber,
            'department': doctor.doctorid.departmentid,
            'license': doctor.license,  
        }
        for doctor in doctors
    ]
    return render(request, 'patient/doctor.html', {'doctor_data': doctor_data})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_nurse(request):
    nurses = models.Nurse.objects.select_related('nurseid')  # Pre-fetch related MedicalStaff
    nurse_data = [
        {
            'nurseid': nurse.nurseid.staffid,
            'fullname': nurse.nurseid.fullname,  
            'dob':nurse.nurseid.staffdob,
            'gender' : nurse.nurseid.gender,
            'phonenumber': nurse.nurseid.phonenumber,
            'department': nurse.nurseid.departmentid,
            'yearexperience': nurse.yearexperience,  
        }
        for nurse in nurses
    ]
    return render(request, 'patient/nurse.html', {'nurse_data': nurse_data})

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_department(request):
    q = """
            SELECT 
                d.departmentid,
                d.departmentname,
                CONCAT(ms.firstname, ' ', ms.midname, ' ', ms.lastname),
                CONCAT(m.startdate, ' - Present')
            FROM manages m
            JOIN department d ON m.departmentid = d.departmentid
            JOIN medical_staff ms ON doctorid = staffid;
            """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()
    manage_data = [
    {
        'id': row[0],
        'name': row[1],
        'headname': row[2],
        'period': row[3]
    }
    for row in rows
    ]
    return render(request, 'patient/department.html', {'manage_data':manage_data})
#################################################################################
#                             for doctor                                        #
#################################################################################
@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_info(request):
    doctor = get_object_or_404(models.MedicalStaff, staffid=request.user.username)
    return render(request, 'doctor/info.html', {'form':doctor})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_doctor(request):
    doctors = models.Doctor.objects.select_related('doctorid')  # Pre-fetch related MedicalStaff
    doctor_data = [
        {
            'doctorid': doctor.doctorid.staffid,
            'fullname': doctor.doctorid.fullname,  
            'dob':doctor.doctorid.staffdob,
            'gender' : doctor.doctorid.gender,
            'phonenumber': doctor.doctorid.phonenumber,
            'department': doctor.doctorid.departmentid,
            'license': doctor.license,  
        }
        for doctor in doctors
    ]
    return render(request, 'doctor/doctor.html', {'doctor_data': doctor_data})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient(request):
   patients = models.Patient.objects.all()
   return render(request, 'doctor/patient.html', {'patients':patients})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_nurse(request):
    nurses = models.Nurse.objects.select_related('nurseid')  # Pre-fetch related MedicalStaff
    nurse_data = [
        {
            'nurseid': nurse.nurseid.staffid,
            'fullname': nurse.nurseid.fullname,  
            'dob':nurse.nurseid.staffdob,
            'gender' : nurse.nurseid.gender,
            'phonenumber': nurse.nurseid.phonenumber,
            'department': nurse.nurseid.departmentid,
            'yearexperience': nurse.yearexperience,  
        }
        for nurse in nurses
    ]
    return render(request, 'doctor/nurse.html', {'nurse_data': nurse_data})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_department(request):
    q = """
            SELECT 
                d.departmentid,
                d.departmentname,
                CONCAT(ms.firstname, ' ', ms.midname, ' ', ms.lastname),
                CONCAT(m.startdate, ' - Present')
            FROM manages m
            JOIN department d ON m.departmentid = d.departmentid
            JOIN medical_staff ms ON doctorid = staffid;
            """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()
    manage_data = [
    {
        'id': row[0],
        'name': row[1],
        'headname': row[2],
        'period': row[3]
    }
    for row in rows
    ]
    return render(request, 'doctor/department.html', {'manage_data':manage_data})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_room(request):
    q = """
            select roomid, capacity, roomtype, GetPatientCountAtRoom(roomid)
            from room
        """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()

    room_data=[
        {
            'roomid':row[0],
            'capacity':row[1],
            'type':row[2],
            'count':row[3]
        }for row in rows
    ]
    return render(request, 'doctor/room.html' ,{'rooms':room_data})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_show_room(request, roomid):
    q = """
            select p.patientid, concat(p.firstname, ' ', p.midname, ' ', p.lastname), 
            p.patientssn, p.patientdob, p.phonenumber, p.gender, concat(p.street, ' ', p.district, ' ', p.city),
            admitteddate, dischargeddate
            from patient p
            join admitted_to at on p.patientid = at.patientid
            where admitteddate <= now() and (dischargedDate > NOW() OR dischargedDate IS NULL) and at.roomid = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(q, [roomid])
        rows = cursor.fetchall()
    room_info = [
        {
            'id':row[0],
            'fullname':row[1],
            'ssn':row[2],
            'dob':row[3],
            'phonenumber':row[4],
            'sex':row[5],
            'adr':row[6],
            'admitted':row[7],
            'discharged':row[8],
        }for row in rows
    ]
    return render(request, 'doctor/show_room.html', {'room_info':room_info, 'roomid':roomid})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_medical_record(request):
    q = """
        select recordid, m.patientid, CONCAT(p.firstname, ' ', p.midname, ' ', p.lastname), recorddate, m.treatmentid, diagnosis, testresult,
        t.treatmentdate, t.treatmentprocedure
        from medical_record m
        join patient p
        on m.patientid = p.patientid
        join treatment t on m.treatmentid = t.treatmentid
        """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()

    medical_record = [
        {
            'recordid':row[0],
            'patientid':row[1],
            'fullname':row[2],
            'date1':row[3],
            'treatmentid':row[4],
            'diagnosis':row[5],
            'result':row[6],
            'date2':row[7],
            'procedure':row[8]
        }for row in rows
    ]

    return render(request, 'doctor/medical_record.html', {'medical_record':medical_record})


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_add_medical_record(request):
    if request.method == 'POST':
        try:
            med_form = forms.MedicalRecord(request.POST)
            treat_form = forms.Treatment(request.POST)
            if med_form.is_valid() and treat_form.is_valid():
                treat_instance = treat_form.save()
                med_instance = med_form.save(commit=False)
                med_instance.treatmentid = treat_instance
                med_instance.save()
                return redirect('doctor-medical-record')
                         
            else:
                return render(request, 'doctor/add_medical_record.html', {'error':'Form is invalid'})
            

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
    med_form = forms.MedicalRecord()
    treat_form = forms.Treatment()
    context = {'med_form':med_form, 'treat_form':treat_form}

    return render(request, 'doctor/add_medical_record.html', context)




@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_edit_medical_record(request, recordid):
        medical_record = get_object_or_404(models.MedicalRecord, recordid=recordid)
        treatment = medical_record.treatmentid

        if request.method == 'POST':
            med_form = forms.MedicalRecord(request.POST, instance=medical_record)
            treat_form = forms.Treatment(request.POST, instance=treatment)

            if med_form.is_valid() and treat_form.is_valid():
                treat_instance = treat_form.save()

                med_instance = med_form.save(commit=False)
                med_instance.treatmentid = treat_instance
                med_instance.save()

                # messages.success(request, 'Medical record updated successfully!')
                return redirect('doctor-medical-record')
            else:
                messages.error(request, 'Form validation failed. Please correct the errors.')

        else:
            med_form = forms.MedicalRecord(instance=medical_record)
            treat_form = forms.Treatment(instance=treatment)

        context = {'med_form': med_form, 'treat_form': treat_form}
        return render(request, 'doctor/edit_medical_record.html', context)


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_delete_medical_record(request, recordid):
    treatment = get_object_or_404(models.Treatment, treatmentid=recordid)
    medical_record = get_object_or_404(models.MedicalRecord, recordid=recordid)
    if request.method == 'POST':
        try:
            treatment.delete()
            medical_record.delete()
            return redirect('doctor-medical-record')
        except Exception as e:
            messages.error(request, f'An unexpected error occurred: {str(e)}')
    context = {'medical_record':medical_record, 'treatment':treatment}
    return render(request, 'doctor/delete_medical_record.html', context)


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_appointment(request):
    appointment = models.Appointment.objects.filter(doctorid=request.user.username)
    return render(request, 'doctor/appointment.html',{'appointment':appointment})
#################################################################################
#                             for nurse                                         #
#################################################################################
@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_info(request):
    nurse = get_object_or_404(models.MedicalStaff, staffid=request.user.username)
    return render(request, 'nurse/info.html', {'form':nurse})




@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_medical_record(request):
    q = """
        select recordid, m.patientid, CONCAT(p.firstname, ' ', p.midname, ' ', p.lastname), recorddate, m.treatmentid, diagnosis, testresult,
        t.treatmentdate, t.treatmentprocedure
        from medical_record m
        join patient p
        on m.patientid = p.patientid
        join treatment t on m.treatmentid = t.treatmentid
        """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()

    medical_record = [
        {
            'recordid':row[0],
            'patientid':row[1],
            'fullname':row[2],
            'date1':row[3],
            'treatmentid':row[4],
            'diagnosis':row[5],
            'result':row[6],
            'date2':row[7],
            'procedure':row[8]
        }for row in rows
    ]

    return render(request, 'nurse/medical_record.html', {'medical_record':medical_record})


@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_add_medical_record(request):
    if request.method == 'POST':
        try:
            med_form = forms.MedicalRecord(request.POST)
            treat_form = forms.Treatment(request.POST)
            if med_form.is_valid() and treat_form.is_valid():
                treat_instance = treat_form.save()
                med_instance = med_form.save(commit=False)
                med_instance.treatmentid = treat_instance
                med_instance.save()
                return redirect('nurse-medical-record')
                         
            else:
                return render(request, 'nurse/add_medical_record.html', {'error':'Form is invalid'})
            

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
    med_form = forms.MedicalRecord()
    treat_form = forms.Treatment()
    context = {'med_form':med_form, 'treat_form':treat_form}

    return render(request, 'nurse/add_medical_record.html', context)




@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_edit_medical_record(request, recordid):
        medical_record = get_object_or_404(models.MedicalRecord, recordid=recordid)
        treatment = medical_record.treatmentid

        if request.method == 'POST':
            med_form = forms.MedicalRecord(request.POST, instance=medical_record)
            treat_form = forms.Treatment(request.POST, instance=treatment)

            if med_form.is_valid() and treat_form.is_valid():
                treat_instance = treat_form.save()

                med_instance = med_form.save(commit=False)
                med_instance.treatmentid = treat_instance
                med_instance.save()

                # messages.success(request, 'Medical record updated successfully!')
                return redirect('nurse-medical-record')
            else:
                messages.error(request, 'Form validation failed. Please correct the errors.')

        else:
            med_form = forms.MedicalRecord(instance=medical_record)
            treat_form = forms.Treatment(instance=treatment)

        context = {'med_form': med_form, 'treat_form': treat_form}
        return render(request, 'nurse/edit_medical_record.html', context)


@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_delete_medical_record(request, recordid):
    treatment = get_object_or_404(models.Treatment, treatmentid=recordid)
    medical_record = get_object_or_404(models.MedicalRecord, recordid=recordid)
    if request.method == 'POST':
        try:
            treatment.delete()
            medical_record.delete()
            return redirect('nurse-medical-record')
        except Exception as e:
            messages.error(request, f'An unexpected error occurred: {str(e)}')
    context = {'medical_record':medical_record, 'treatment':treatment}
    return render(request, 'nurse/delete_medical_record.html', context)


@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_doctor(request):
    doctors = models.Doctor.objects.select_related('doctorid')  # Pre-fetch related MedicalStaff
    doctor_data = [
        {
            'doctorid': doctor.doctorid.staffid,
            'fullname': doctor.doctorid.fullname,  
            'dob':doctor.doctorid.staffdob,
            'gender' : doctor.doctorid.gender,
            'phonenumber': doctor.doctorid.phonenumber,
            'department': doctor.doctorid.departmentid,
            'license': doctor.license,  
        }
        for doctor in doctors
    ]
    return render(request, 'nurse/doctor.html', {'doctor_data': doctor_data})

@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_patient(request):
   patients = models.Patient.objects.all()
   return render(request, 'nurse/patient.html', {'patients':patients})


@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_nurse(request):
    nurses = models.Nurse.objects.select_related('nurseid')  # Pre-fetch related MedicalStaff
    nurse_data = [
        {
            'nurseid': nurse.nurseid.staffid,
            'fullname': nurse.nurseid.fullname,  
            'dob':nurse.nurseid.staffdob,
            'gender' : nurse.nurseid.gender,
            'phonenumber': nurse.nurseid.phonenumber,
            'department': nurse.nurseid.departmentid,
            'yearexperience': nurse.yearexperience,  
        }
        for nurse in nurses
    ]
    return render(request, 'nurse/nurse.html', {'nurse_data': nurse_data})

@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_department(request):
    q = """
            SELECT 
                d.departmentid,
                d.departmentname,
                CONCAT(ms.firstname, ' ', ms.midname, ' ', ms.lastname),
                CONCAT(m.startdate, ' - Present')
            FROM manages m
            JOIN department d ON m.departmentid = d.departmentid
            JOIN medical_staff ms ON doctorid = staffid;
            """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()
    manage_data = [
    {
        'id': row[0],
        'name': row[1],
        'headname': row[2],
        'period': row[3]
    }
    for row in rows
    ]
    return render(request, 'nurse/department.html', {'manage_data':manage_data})


@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_room(request):
    q = """
            select roomid, capacity, roomtype, GetPatientCountAtRoom(roomid)
            from room
        """
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()

    room_data=[
        {
            'roomid':row[0],
            'capacity':row[1],
            'type':row[2],
            'count':row[3]
        }for row in rows
    ]
    return render(request, 'nurse/room.html' ,{'rooms':room_data})


@login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_show_room(request, roomid):
    q = """
            select p.patientid, concat(p.firstname, ' ', p.midname, ' ', p.lastname), 
            p.patientssn, p.patientdob, p.phonenumber, p.gender, concat(p.street, ' ', p.district, ' ', p.city),
            admitteddate, dischargeddate
            from patient p
            join admitted_to at on p.patientid = at.patientid
            where admitteddate <= now() and (dischargedDate > NOW() OR dischargedDate IS NULL) and at.roomid = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(q, [roomid])
        rows = cursor.fetchall()
    room_info = [
        {
            'id':row[0],
            'fullname':row[1],
            'ssn':row[2],
            'dob':row[3],
            'phonenumber':row[4],
            'sex':row[5],
            'adr':row[6],
            'admitted':row[7],
            'discharged':row[8],
        }for row in rows
    ]
    return render(request, 'nurse/show_room.html', {'room_info':room_info, 'roomid':roomid})