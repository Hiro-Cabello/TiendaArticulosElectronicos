from rest_framework import serializers
#Los serializadores convertir los datos complejos como QuerySets o instancias de modelos a tipos de datos
#de Python nativas que luego pueden ser facilmente tranmitidas en JSON ,XML u otros contenidos.
from django.contrib.auth.models import User
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'