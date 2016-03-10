from django.shortcuts import render

def pressure_list(request):
    return render(request, 'pressure/pressure_list.html', {})
