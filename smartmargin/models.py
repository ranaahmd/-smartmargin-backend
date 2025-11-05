from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profit_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('30.00'))
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    profit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def calculate_costs(self):
        ingredients = self.productingredient_set.all()
        total = sum(
            i.ingredient.cost_per_unit * i.quantity for i in ingredients
        )
        self.total_cost = total
        self.profit_amount = (self.total_cost * self.profit_percentage) / 100
        self.selling_price = self.total_cost + self.profit_amount
    def save(self, *args, **kwargs):
     super().save(*args, **kwargs)
     if not kwargs.get('update_fields'):
        self.calculate_costs()
        super().save(update_fields=['total_cost', 'profit_amount', 'selling_price'])

class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.save()

    def delete(self, *args, **kwargs):
        product = self.product
        super().delete(*args, **kwargs)
        product.save()
    def update_product_costs(sender, instance, **kwargs):
     product = instance.product
     ingredients = product.productingredient_set.all()
     total = sum(i.ingredient.cost_per_unit * i.quantity for i in ingredients)
     product.total_cost = total
     product.profit_amount = total * (product.profit_percentage / 100)
     product.selling_price = total + product.profit_amount
     product.save(update_fields=['total_cost', 'profit_amount', 'selling_price'])

class Note (models.Model):
    title = models.CharField(max_length=100)
    content= models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"
