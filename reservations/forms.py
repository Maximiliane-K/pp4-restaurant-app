from django import forms
from django.contrib.auth.models import User


class BookingForm(forms.Form):
    date_time = forms.DateTimeField(label='Date and Time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    num_people = forms.IntegerField(label='Number of People')


#class RegistrationForm(forms.ModelForm):
   # password = forms.CharField(label='Password', widget=forms.PasswordInput)

    #class Meta:
      #  model = User
       # fields = ['username', 'email']

