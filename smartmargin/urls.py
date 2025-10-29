from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    
)
from .views import *
urlpatterns =[
    path ('ingredients/',IngredientListViewSet.as_view(),name='Ingredients-list'),
    path ('ingredients/<int:id>/',IngredientDeatailAPIView.as_view(),name='Ingredients-detail'),
    path ('products/',ProductListAPIView.as_view(),name='products-list'),
    path('products/<int:id>/',ProductDeatailAPIView.as_view(),name='products-detail'),
    path('notes/',NoteListCreateAPIView.as_view(),name='note-list'),
    path('notes/<int:id>/',NoeDetailAPITView.as_view(),name='note-detail'),
    #copied from george
    path('signup/', views.SignupUserView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('api/logout/', views.LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]