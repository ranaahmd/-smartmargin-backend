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
    
        