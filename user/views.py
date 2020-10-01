from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import patientregisterform , Userregister
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import patient
from django.views import generic
from django.views.generic.edit import FormView
<<<<<<< HEAD
from rest_framework import viewsets
from user.serializers import PatientSerializer
=======
from django.core.mail import send_mail
>>>>>>> upstream/master


# Create your views here.

def patientregister_view(request):
    if request.method == 'POST':
        form = patientregisterform(request.POST)
        if form.is_valid():
            form.save()
            namee = form.cleaned_data['name']
            emaile = form.cleaned_data['email']
            subject =  f'{namee} is registered as Patient at Hospipro'
            message = f'Hello {namee} this is Auto-generated mail you can now view your profile at '
            from_email = 'teameureka2k19@gmail.com'
            to_list = [emaile]
            send_mail(subject , message , from_email , to_list , fail_silently=False)
            messages.success(request,'Patient created sucessfully')
            return redirect('/')
    else:
        form = patientregisterform()
    return render(request, 'user/addpatient.html',{'form':form})
def create_user(request):
    if request.method == 'POST':
        form = Userregister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created sucessfully')
            return redirect('login')
    else:
        form = Userregister()
    return render(request, 'user/register.html',{'form':form})
class profileview(generic.DetailView):
    model = patient
    template_name = 'user/profile.html'
class patientupdateview(LoginRequiredMixin,generic.UpdateView):
    model = patient
    fields = ['diseases','alergy','report']
    template_name_suffix = '_update_form'
    def form_valid(self,form):
        return super().form_valid(form)

class apiview(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = PatientSerializer


