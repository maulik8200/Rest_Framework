from rest_framework import serializers
from .models import *

class PerfumeSerializer(serializers.ModelSerializer):

    class Meta:

        model  =  Perfume
        fields  = '__all__'