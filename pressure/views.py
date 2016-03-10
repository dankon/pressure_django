from django.shortcuts import render
from .models import BloodPressure

def pressure_list(request):
    all_blood_pressure = BloodPressure.objects.all().order_by('-add_date_time')
    return render(request, 'pressure/pressure_list.html', 
                  {'all_bl_press' : all_blood_pressure})