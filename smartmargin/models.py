from django.db import models
from django.contrib.auth.models import User
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    cost_per_unit=models.DecimalField(max_digits=10,decimal_places=2)
    unit =models.CharField(max_length=20)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)