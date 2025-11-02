from django.db import models
from django.contrib.auth.models import User
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    cost_per_unit=models.DecimalField(max_digits=10,decimal_places=2)
    unit =models.CharField(max_length=20)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
class Product(models.Model):
    name = models.CharField(max_length=100)
    profit_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient,through='ProductIngredient')
    created = models.DateTimeField(auto_now_add=True)
class ProductIngredient(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    ingredient =models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
class Note (models.Model):
    title = models.CharField(max_length=100)
    content= models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)