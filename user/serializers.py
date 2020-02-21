from rest_framework import serializers
from user.models import patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = patient
        fields = ('name','email','age','bloodgroup','diseases','medihistory','alergy','report')