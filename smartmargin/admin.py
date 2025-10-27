from django.contrib import admin
from .models import Product,ProductIngredient,Note,Ingredient
admin.site.register(ProductIngredient)
admin.site.register(Note)
admin.site.register(Product)
admin.site.register(Ingredient)
