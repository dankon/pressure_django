#-*- coding: utf-8 -*-
#!/usr/bin/env python
from django.forms import ModelForm

from .models import BloodPressure

class BloodAddingForm(ModelForm):


    class Meta:
        model = BloodPressure
        fields = ('systolic_value', 
                  'diastolic_value', 
                  'pulse',
                  'comment',
                  'add_date_time'
                  )