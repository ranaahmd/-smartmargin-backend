from django.urls import path
from .views import (
    IngredientDeatailAPIView,IngredientListViewSet,ProductListAPIView,ProductDeatailAPIView,NoeDetailAPITView,NoteListCreateAPIView
)
urlpatterns =[
    path ('ingredients/',IngredientListViewSet.as_view(),name='Ingredients-list'),
    path ('ingredients/<int:id>/',IngredientDeatailAPIView.as_view(),name='Ingredients-detail'),
    path ('products/',ProductListAPIView.as_view(),name='products-list'),
    path('products/<int:id>/',ProductDeatailAPIView.as_view(),name='products-detail'),
    path('notes/',NoteListCreateAPIView.as_view(),name='note-list'),
    path('notes/<int:id>/',NoeDetailAPITView.as_view(),name='note-detail')
]