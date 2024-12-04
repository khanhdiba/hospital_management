from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
from . import forms
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

# def login_page_patient(request):
#   if request.method == "POST":
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#       login(request, user)
#       return redirect('main_page')
#     else:
#       messages.success(request, ("The credentials you provided cannot be determined to be authentic."))
#       return redirect('patient_login')
#   return render(request, 'patientlogin.html', {})

# def admin_login_page(request):
#   if request.method == "POST":
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#       login(request, user)
#       return redirect('dashboard')
#     else:
#       messages.success(request, ("The credentials you provided cannot be determined to be authentic."))
#       return redirect('admin_login')
#   return render(request, 'adminlogin.html', {})

# def recep_login_page(request):
#   if request.method == "POST":
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#       login(request, user)
#       return redirect('main_page')
#     else:
#       messages.success(request, ("The credentials you provided cannot be determined to be authentic."))
#       return redirect('recep_login')
#   return render(request, 'receplogin.html', {})

# def doctor_login_page(request):
#   if request.method == "POST":
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#       login(request, user)
#       return redirect('main_page')
#     else:
#       messages.success(request, ("The credentials you provided cannot be determined to be authentic."))
#       return redirect('doctor_login')
#   return render(request, 'docorlogin.html', {})

# def nurse_login_page(request):
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
