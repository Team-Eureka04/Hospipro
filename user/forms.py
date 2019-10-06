from django.contrib.auth.models import User
from user.models import patient
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Userregister(UserCreationForm):
    Email = forms.EmailField()

    class meta:
        model = User
        fields = ['username','Email','password1','password2']
class patientregisterform(forms.ModelForm):
    class Meta:
        model = patient
        fields = ('name','email','age','bloodgroup','diseases','medihistory','alergy','report')
