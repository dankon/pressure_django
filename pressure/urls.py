from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pressure_list, name='pressure_list'),
]