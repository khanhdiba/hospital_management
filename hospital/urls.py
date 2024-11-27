from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('patientclick', views.patient_click_page),
    path('hospitalstaffclick', views.hos_staff_click_page),
    path('hospitalstaffclick/adminclick', views.admin_click_page),
    path('hospitalstaffclick/recepclick', views.recep_click_page),
    path('hospitalstaffclick/doctorclick', views.doctor_click_page),
    path('hospitalstaffclick/nurseclick', views.nurse_click_page),
    path('aboutus', views.about_us),
]