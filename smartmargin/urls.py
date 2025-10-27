from django.urls import path
from .views import (
    IngredientDeatailAPIView
)
urlpatterns =[
    path('ingredients/',IngredientDeatailAPIView.as_view(),name="inredient-detail")
]