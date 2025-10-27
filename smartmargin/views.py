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
class IngredientDeatailAPIView(APIView):
    permission_classes =[permissions.IsAuthenticated]
    def  get_object(self,id,user):
        try:
            return Ingredient.objects.get(id=id,user=user)
        except Ingredient.DoesNotExist:
            return None
    def get(self,request,id):
      ingredient = self.get_object(id,request.user)
      if not ingredient:
          return Response({"error:" :"Ingredent not found"},status=status.HTTP_404_NOT_FOUND)
      serializer = IngredientSerializer(ingredient)
      return Response(serializer.data)
    def put (self,request,id):
        ingredient = self.get_object(id,request.user)
        if not ingredient:
             return Response({"error:" :"Ingredent not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = IngredientSerializer(ingredient,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,id,request):
        ingredient = self.get_object(id,request.user)
        if not ingredient:
             return Response({"error:" :"Ingredent not found"},status=status.HTTP_404_NOT_FOUND)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)