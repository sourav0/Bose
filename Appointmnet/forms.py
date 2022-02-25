from dataclasses import field
from email.policy import default
from django import forms
import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Appointment
class DateInput(forms.DateInput):
    input_type = 'date' 



class AppoinmentModelForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date_field': DateInput(),
        }
# class AppoinmentForm(forms.Form):
#     first_name = forms.CharField(max_length=101)
#     last_name = forms.CharField(max_length=101)
#     email = forms.EmailField()

#     address_line1 = forms.CharField(max_length=256)
#     city = forms.CharField(max_length=25)
#     state = forms.CharField(max_length=25)
#     pincode = forms.IntegerField()

#     date_field = forms.DateField(label='Date Field',initial=datetime.date.today,label_suffix=" : ",
#                              required=True, disabled=False, input_formats=["%d-%m-%Y"],
#                              widget=forms.DateInput(attrs={'class': 'form-control'}),
#                              error_messages={'required': "This field is required."})
#     time_field = forms.TimeField(label='Time Field',initial=datetime.time, label_suffix=" : ",
#                              required=True, disabled=False, input_formats=["%H:%M:%S"],
#                              widget=forms.TimeInput(attrs={'class': 'form-control'}),
#                              error_messages={'required': "This field is required."})
#     class Meta:
#         model = User
#         fields ='__all__'
#         # fields = ['register_as','username', 'first_name', 'last_name', 'email','profile_picture', 'password1', 'password2','address_line1','city','state','pincode']


