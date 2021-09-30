from django.db.models import fields
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
        
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)