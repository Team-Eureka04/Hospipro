from django.db import models
from django.urls import reverse

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=20 , decimal_places=0)
    email = models.EmailField(max_length=250)
    diseases = models.CharField(max_length=200,null=True , blank=True)
    bloodgroup = models.CharField(max_length=100,default='no-value')
    medihistory = models.TextField(max_length=500,default='no history')
    alergy = models.CharField(max_length=100,null=True,blank=True)
    report = models.ImageField(default='default.jpg',upload_to='report_pics')
    

    def __str__(self):
        return f'{self.name} Profile'
    def get_absolute_url(self):
        return reverse('profile',kwargs={'pk':self.pk})





    