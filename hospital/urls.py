from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('patientclick', views.patient_click_page),
    path('hospitalstaffclick', views.hos_staff_click_page),
    path('hospitalstaffclick/adminclick', views.admin_click_page),
    path('hospitalstaffclick/recepclick', views.recep_click_page),
    path('hospitalstaffclick/doctorclick', views.doctor_click_page),
    path('hospitalstaffclick/nurseclick', views.nurse_click_page),
    path('aboutus', views.about_us),

    # path('patientlogin', views.login_page_patient, name='patient_login'),
    # path('hospitalstaffclick/adminclick/login', views.admin_login_page, name='admin_login'),
    # path('hospitalstaffclick/recepclick/login', views.recep_login_page, name='recep_login'),
    # path('hospitalstaffclick/doctorclick/login', views.doctor_login_page, name='doctor_login'),
    # path('hospitalstaffclick/nurseclick/login', views.nurse_login_page, name='nurse_login'),

    path('patientsignup', views.patient_signup_view, name='patient_signup'),
    path('doctorsignup', views.doctor_signup_view, name='doctor_signup'),
    path('nursesignup', views.nurse_signup_view, name='nurse_signup'),
    path('adminsignup', views.admin_signup_view, name='admin_signup'),
    path('recepsignup', views.recep_signup_view, name='recep_signup'),


    path('patientlogin', LoginView.as_view(template_name='patientlogin.html'), name='patient_login'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'), name='admin_login'),
    path('receplogin', LoginView.as_view(template_name='receplogin.html'), name='recep_login'),
    path('doctorlogin', LoginView.as_view(template_name='doctorlogin.html'), name='doctor_login'),
    path('nurselogin', LoginView.as_view(template_name='nurselogin.html'), name='nurse_login'),
    
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='main_page.html'),name='logout'),

    path('patient-dashboard', views.patient_dashboard, name='patient-dashboard'),
    path('recep-dashboard', views.recep_dashboard, name='recep-dashboard'),
    path('doctor-dashboard', views.doctor_dashboard, name='doctor-dashboard'),
    path('nurse-dashboard', views.nurse_dashboard, name='nurse-dashboard'),
    path('admin-dashboard', views.admin_dashboard, name='admin-dashboard'),
    
    
]

############################################################################
#####################FOR ADMIN##############################################
############################################################################

urlpatterns += [
    path('admin-patient', views.admin_patient, name='admin-patient'),
    path('admin-add-patient', views.admin_add_patient, name='admin-add-patient'),
    path('admin-delete-patient/<str:patientid>/', views.admin_delete_patient, name='admin-delete-patient'),
    path('admin-edit-patient/<str:patientid>/', views.admin_edit_patient, name='admin-edit-patient'),

    path('admin-appointment', views.admin_appointment, name='admin-appointment'),
    path('admin-delete-appointment/<int:appointmentid>/', views.admin_delete_appointment, name='admin-delete-appointment'),
    path('admin-edit-appointment/<int:appointmentid>/', views.admin_edit_appointment, name='admin-edit-appointment'),
    path('admin-add-appointment', views.admin_add_appointment, name='admin-add-appointment'),

]


############################################################################
#####################FOR DOCTOR#############################################
############################################################################


############################################################################
#####################FOR NURSE##############################################
############################################################################


############################################################################
#####################FOR PATIENT############################################
############################################################################


############################################################################
#####################FOR RECEPTIONIST#######################################
############################################################################

urlpatterns += [
    path('recep-admit', views.recep_admit, name='recep-admit'),
    path('recep-add-patient', views.recep_add_patient, name='recep-add-patient'),
    path('recep-delete-patient/<str:patientid>/', views.recep_delete_patient, name='recep-delete-patient'),
    path('recep-edit-patient/<str:patientid>/', views.recep_edit_patient, name='recep-edit-patient'),

    path('recep-appointment', views.recep_appointment, name='recep-appointment'),
    path('recep-delete-appointment/<int:appointmentid>/', views.recep_delete_appointment, name='recep-delete-appointment'),
    path('recep-edit-appointment/<int:appointmentid>/', views.recep_edit_appointment, name='recep-edit-appointment'),
    path('recep-add-appointment', views.recep_add_appointment, name='recep-add-appointment'),

]