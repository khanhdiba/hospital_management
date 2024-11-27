from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

def main_page(request):
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

