from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from .models import Ingredient,Product,ProductIngredient,Note
from .serializers import IngredientSerializer ,ProductSerializer,ProductIngredientSerializer,NoteSerializer
class IngredientViewSet(APIView):
    permission_classes =[permissions.IsAuthenticated]
    def get(self,request):
        Ingredients = Ingredient.objects.filter(user=self.request.user) 
        serializer= IngredientSerializer(Ingredients,many=True) 
        return Response(serializer.data)
    def post(self,request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)