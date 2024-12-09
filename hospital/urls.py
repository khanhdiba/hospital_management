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

    path('admin-doctor', views.admin_doctor, name='admin-doctor'),
    path('admin-add-doctor', views.admin_add_doctor, name='admin-add-doctor'),
    path('admin-delete-doctor/<str:staffid>/', views.admin_delete_doctor, name='admin-delete-doctor'),
    path('admin-edit-doctor/<str:doctorid>/', views.admin_edit_doctor, name='admin-edit-doctor'),


    path('admin-nurse', views.admin_nurse, name='admin-nurse'),
    path('admin-add-nurse', views.admin_add_nurse, name='admin-add-nurse'),
    path('admin-delete-nurse/<str:staffid>/', views.admin_delete_nurse, name='admin-delete-nurse'),
    path('admin-edit-nurse/<str:nurseid>/', views.admin_edit_nurse, name='admin-edit-nurse'),

    path('admin-department', views.admin_department, name='admin-department'),
    path('admin-medical-record', views.admin_medical_record, name='admin-medical-record'),
    path('admin-add-medical-record', views.admin_add_medical_record, name='admin-add-medical-record'),
    path('admin-edit-medical-record/<int:recordid>/', views.admin_edit_medical_record, name='admin-edit-medical-record'),
    path('admin-delete-medical-record/<int:recordid>/', views.admin_delete_medical_record, name='admin-delete-medical-record'),

    path('admin-room', views.admin_room, name='admin-room'),
    path('admin-add-room/<str:roomid>/', views.admin_add_room, name='admin-add-room'),
    path('admin-show-room/<str:roomid>/', views.admin_show_room, name='admin-show-room')

]

############################################################################
#####################FOR RECEPTIONIST#######################################
############################################################################

urlpatterns += [
    path('recep-patient', views.recep_patient, name='recep-patient'),
    path('recep-add-patient', views.recep_add_patient, name='recep-add-patient'),
    path('recep-delete-patient/<str:patientid>/', views.recep_delete_patient, name='recep-delete-patient'),
    path('recep-edit-patient/<str:patientid>/', views.recep_edit_patient, name='recep-edit-patient'),

    path('recep-appointment', views.recep_appointment, name='recep-appointment'),
    path('recep-delete-appointment/<int:appointmentid>/', views.recep_delete_appointment, name='recep-delete-appointment'),
    path('recep-edit-appointment/<int:appointmentid>/', views.recep_edit_appointment, name='recep-edit-appointment'),
    path('recep-add-appointment', views.recep_add_appointment, name='recep-add-appointment'),

    path('recep-doctor', views.recep_doctor, name='recep-doctor'),
    path('recep-nurse', views.recep_nurse, name='recep-nurse'),
    path('recep-department', views.recep_department, name='recep-department'),

    path('recep-room', views.recep_room, name='recep-room'),
    path('recep-add-room/<str:roomid>/', views.recep_add_room, name='recep-add-room'),
    path('recep-show-room/<str:roomid>/', views.recep_show_room, name='recep-show-room')

]


###############################################################################
#           for patient         #
urlpatterns += [
    path('patient-info', views.patient_info, name='patient-info'),
    path('patient-health', views.patient_health, name='patient-health'),
    path('patient-appointment', views.patient_appointment, name='patient-appointment'),
    path('patient-add-appointment', views.patient_add_appointment, name='patient-add-appointment'),
    path('patient-room', views.patient_room, name='patient-room'),
    path('patient-doctor', views.patient_doctor, name='patient-doctor'),
    path('patient-nurse', views.patient_nurse, name='patient-nurse'),
    path('patient-department', views.patient_department, name='patient-department'),
]



#Doctor
urlpatterns += [
    path('doctor-info', views.doctor_info, name='doctor-info'),
    path('doctor-doctor', views.doctor_doctor, name='doctor-doctor'),
    path('doctor-nurse', views.doctor_nurse, name='doctor-nurse'),
    path('doctor-patient', views.doctor_patient, name='doctor-patient'),
    path('doctor-department', views.doctor_department, name='doctor-department'),
    path('doctor-room', views.doctor_room, name='doctor-room'),
    path('doctor-show-room/<str:roomid>/', views.doctor_show_room, name='doctor-show-room'),

    path('doctor-medical-record', views.doctor_medical_record, name='doctor-medical-record'),
    path('doctor-add-medical-record', views.doctor_add_medical_record, name='doctor-add-medical-record'),
    path('doctor-edit-medical-record/<int:recordid>/', views.doctor_edit_medical_record, name='doctor-edit-medical-record'),
    path('doctor-delete-medical-record/<int:recordid>/', views.doctor_delete_medical_record, name='doctor-delete-medical-record'),
    path('doctor-appointment', views.doctor_appointment, name='doctor-appointment')

]


#Nurse
urlpatterns += [
    path('nurse-info', views.nurse_info, name='nurse-info'),
    path('nurse-medical-record', views.nurse_medical_record, name='nurse-medical-record'),
    path('nurse-add-medical-record', views.nurse_add_medical_record, name='nurse-add-medical-record'),
    path('nurse-edit-medical-record/<int:recordid>/', views.nurse_edit_medical_record, name='nurse-edit-medical-record'),
    path('nurse-delete-medical-record/<int:recordid>/', views.nurse_delete_medical_record, name='nurse-delete-medical-record'),
    path('nurse-doctor', views.nurse_doctor, name='nurse-doctor'),
    path('nurse-nurse', views.nurse_nurse, name='nurse-nurse'),
    path('nurse-patient', views.nurse_patient, name='nurse-patient'),
    path('nurse-department', views.nurse_department, name='nurse-department'),

    path('nurse-room', views.nurse_room, name='nurse-room'),
    path('nurse-show-room/<str:roomid>/', views.nurse_show_room, name='nurse-show-room'),
]