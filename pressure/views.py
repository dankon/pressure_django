from django.shortcuts import render, redirect
from .models import BloodPressure
from .forms import BloodAddingForm

def pressure_list(request):
    all_blood_pressure = BloodPressure.objects.all().order_by('-add_date_time')
    return render(request, 'pressure/pressure_list.html', 
                  {'all_bl_press' : all_blood_pressure})
                
def blood_pressure_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BloodAddingForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('pressure_list')
        else:
            form = BloodAddingForm()
            return render(request, 'pressure/pressure_add.html', {'form' : form})
    else:
        return redirect('pressure_list')