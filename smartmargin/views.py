from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status,permissions,generics
from .models import Ingredient,Product,ProductIngredient,Note
from .serializers import UserSerializer
from .serializers import IngredientSerializer ,ProductSerializer,ProductIngredientSerializer,NoteSerializer
class IngredientListViewSet(APIView):
    permission_classes =[permissions.IsAuthenticated]
    def get(self,request):
        ingredients = Ingredient.objects.filter(user=self.request.user) 
        serializer= IngredientSerializer(ingredients,many=True) 
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
class ProductListAPIView(APIView):
     permission_classes =[permissions.IsAuthenticated]
     def get_object(self,request):
        products = Product.objects.filter(user=request.user)
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
     def post (self,request):
         serializer= ProductSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save(user=request.user)
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
class ProductDeatailAPIView (APIView):
    permission_classes =[permissions.IsAuthenticated]
    def get_object(self,id,user):
        try:
            return Product.objects.get(id=id,user=user)
        except Product.DoesNotExist:
            return None
    def get(self,request,id):
      Product = self.get_object(id,request.user)
      if not Product:
          return Response({"error:" :"Product not found"},status=status.HTTP_404_NOT_FOUND)
      serializer = ProductSerializer(Product)
      return Response(serializer.data)
    def put (self,request,id):
        Product = self.get_object(id,request.user)
        if not Product:
             return Response({"error:" :"Product not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(Product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,id,request):
        Product = self.get_object(id,request.user)
        if not Product:
             return Response({"error:" :"Product not found"},status=status.HTTP_404_NOT_FOUND)
        Product.delete()
class NoteListCreateAPIView(APIView):
     permission_classes =[permissions.IsAuthenticated]
     def get_object(self,request):
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data)
     def post (self,request):
         serializer= NoteSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save(user=request.user)
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
class NoeDetailAPITView(APIView):
       permission_classes =[permissions.IsAuthenticated]
       def get_object(self,id,user):
        try:
            return Note.objects.get(id=id,user=user)
        except Note.DoesNotExist:
            return None
       def get(self,request,id):
        note = self.get_object(id,request.user)
        if not note:
          return Response({"error:" :"Note not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
       def put (self,request,id):
        note = self.get_object(id,request.user)
        if not note:
             return Response({"error:" :"Note not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(Note,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
       def delete(self,id,request):
        note = self.get_object(id,request.user)
        if not Note:
             return Response({"error:" :"Note not found"},status=status.HTTP_404_NOT_FOUND)
        note.delete()
 #copied from cat-collector
class SignupUserView(APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
class LogoutView(APIView):
     permission_classes = [permissions.AllowAny]
     serializer_class = [JWTAuthentication]
     def post (self,request):
         try:
             refresh_token = request.data["refresh"]
             token = RefreshToken(refresh_token)
             token.blacklist()
             return Response({"message:":"Logout "},status=status.HTTP_205_RESET_CONTENT)
         except Exception as e:
             return Response ({"error:",str(e)}, status=status.HTTP_400_BAD_REQUEST)
