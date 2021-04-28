from rest_framework import serializers
from .models import Appdata

class appSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appdata
        fields = ('name','email','vehicleNumber')

        