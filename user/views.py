from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import patientregisterform , Userregister
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import patient
from django.views import generic
from django.views.generic.edit import FormView
from django.core.mail import send_mail


# Create your views here.

def patientregister_view(request):
    if request.method == 'POST':
        form = patientregisterform(request.POST)
        if form.is_valid():
            form.save()
            subject = 'You are registered as Patient at Hospipro'
            message = 'Hello is conformation mail'
            from_email = settings.EMAIL_HOST_USER
            to_list = ['limbaninishit130@gmail.com']
            send_mail(subject , message , from_email , to_list , fail_silently=True)
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
# def profileview(request):
#     obj = patient.objects.get(id=2)
#     return render(request ,"user/profile.html" , {
#     "object":obj,
#      })
class profileview(generic.DetailView):
    model = patient
    template_name = 'user/profile.html'
class patientupdateview(LoginRequiredMixin,generic.UpdateView):
    model = patient
    fields = ['diseases','alergy','report']
    template_name_suffix = '_update_form'
    def form_valid(self,form):
        return super().form_valid(form)


