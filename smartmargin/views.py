from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status,permissions,generics
from .models import Ingredient,Product,ProductIngredient,Note,Dashboard
from .serializers import UserSerializer
from .serializers import IngredientSerializer ,ProductSerializer,ProductIngredientSerializer,NoteSerializer,DashboardSerializer

class IngredientListViewSet(APIView):
    permission_classes =[permissions.IsAuthenticated]
    def get(self,request):
        ingredients = Ingredient.objects.filter(user=request.user) 
        serializer= IngredientSerializer(ingredients,many=True, context={'request': request}) 
        return Response(serializer.data)
    def post(self,request):
        serializer = IngredientSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
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
      serializer = IngredientSerializer(ingredient, context={'request': request})
      return Response(serializer.data)
    def put (self,request,id):
        ingredient = self.get_object(id,request.user)
        if not ingredient:
             return Response({"error:" :"Ingredent not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = IngredientSerializer(ingredient,data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        ingredient = self.get_object(id,request.user)
        if not ingredient:
             return Response({"error:" :"Ingredent not found"},status=status.HTTP_404_NOT_FOUND)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductListAPIView(APIView):
     permission_classes =[permissions.IsAuthenticated]
     def get(self,request):
        products = Product.objects.filter(user=request.user)
        serializer = ProductSerializer(products,many=True, context={'request': request})
        return Response(serializer.data)
     def post (self,request):
         serializer= ProductSerializer(data=request.data, context={'request': request})
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class DashboardAPIView(APIView) :
    permission_classes =[permissions.IsAuthenticated]
    def get(self,request):
        dashboards = Dashboard.objects.filter(user=request.user)
        serializer = DashboardSerializer(dashboards,many=True, context={'request': request})
        return Response(serializer.data)
    def post (self,request):
         serializer= DashboardSerializer(data=request.data, context={'request': request})
         if serializer.is_valid():
             serializer.save()
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
      product = self.get_object(id,request.user)
      if not product:
          return Response({"error:" :"Product not found"},status=status.HTTP_404_NOT_FOUND)
      serializer = ProductSerializer(product, context={'request': request})
      return Response(serializer.data)
    def put (self,request,id):
        product = self.get_object(id,request.user)
        if not product:
             return Response({"error:" :"Product not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product,data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        product = self.get_object(id,request.user)
        if not product:
             return Response({"error:" :"Product not found"},status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NoteListCreateAPIView(APIView):
     permission_classes =[permissions.IsAuthenticated]
     def get(self,request):
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializer(notes,many=True, context={'request': request})
        return Response(serializer.data)
     def post (self,request):
         serializer= NoteSerializer(data=request.data, context={'request': request})
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
class NoteDetailAPITView(APIView):
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
        serializer = NoteSerializer(note, context={'request': request})
        return Response(serializer.data)
       def put (self,request,id):
        note = self.get_object(id,request.user)
        if not note:
             return Response({"error:" :"Note not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note,data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
       def delete(self,request,id):
        note = self.get_object(id,request.user)
        if not note:
             return Response({"error:" :"Note not found"},status=status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SignupUserView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password or not email:
            return Response(
                {"error": "All fields are required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Email already exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
      
        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            serializer = UserSerializer(user)
            return Response(
                {"message": "User created successfully", "user": serializer.data},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        from django.contrib.auth import authenticate
        from rest_framework_simplejwt.tokens import RefreshToken
        
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response(
                {"error": "Invalid credentials"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )