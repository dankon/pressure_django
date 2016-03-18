from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pressure_list, name='pressure_list'),
    url(r'^blood_pressure/new/$', views.blood_pressure_new, name='blood_pressure_new'),
]