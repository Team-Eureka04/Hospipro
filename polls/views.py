from django.shortcuts import render
from django.http import HttpResponse
from user.models import patient
from django.views.generic import ListView


# def index(request,*args, **kwargs):
#    obj = patient.objects.all()
#    return render(request ,"home.html" , {
#       "object":obj,
#    })
class index(ListView):
   model = patient
   template_name = 'home.html'
   context_object_name = 'object'
