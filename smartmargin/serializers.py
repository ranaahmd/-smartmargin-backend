from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ingredient, Product, ProductIngredient, Note

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        return super().update(instance, validated_data)

class ProductIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())

    class Meta:
        model = ProductIngredient
        fields = ['ingredient', 'quantity']


class ProductSerializer(serializers.ModelSerializer):
    ingredients = ProductIngredientSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['user']


    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        validated_data['user'] = self.context['request'].user
        product = Product.objects.create(**validated_data)
        for ing in ingredients_data:
            ProductIngredient.objects.create(product=product, **ing)
        product.refresh_from_db()
        product.calculate_costs()
        product.save(update_fields=['total_cost', 'profit_amount', 'selling_price'])
        return product

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', None)
        validated_data.pop('user', None)
        instance = super().update(instance, validated_data)
        if ingredients_data is not None:
            instance.productingredient_set.all().delete()
            for ing in ingredients_data:
                ProductIngredient.objects.create(product=instance, **ing)
        instance.refresh_from_db()
        instance.calculate_costs()
        instance.save(update_fields=['total_cost', 'profit_amount', 'selling_price'])
        return instance

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
