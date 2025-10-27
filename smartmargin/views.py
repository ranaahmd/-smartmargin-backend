from rest_framework import viewsets,permissions
from .models import Ingredient,Product,ProductIngredient,Note
from .serializers import IngredientSerializer ,ProductSerializer,ProductIngredientSerializer,NoteSerializer
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes =[permissions.IsAuthenticated]
    def get_queryset(self):
        return Ingredient.objects.filter(user=self.request.user) 
    def perform_create(self, serializer):
       serializer.save(user=self.request.user)
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes =[permissions.IsAuthenticated]
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
         serializer.save(user=self.request.user)
class ProductIngredientViewSet(viewsets.ModelViewSet):
    queryset = ProductIngredient.objects.all()
    serializer_class =ProductIngredientSerializer
    permission_classes =[permissions.IsAuthenticated]