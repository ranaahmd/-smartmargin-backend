from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ingredient,Product,ProductIngredient,Note
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model =Ingredient
        fields = '__all__'
class ProductIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductIngredient
        fields ='__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class NoteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Note
        fields ='__all__'
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(w)