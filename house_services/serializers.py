from rest_framework import serializers

from . import models


class House_serviceImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.House_serviceImage
        fields = '__all__'


class House_serviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.House_service
        fields = '__all__'