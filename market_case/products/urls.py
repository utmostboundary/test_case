from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('products/', views.ProductsAPIList.as_view(), name='products'),
    path('products/<pk>/', views.ProductDetailView.as_view(), name='product'),
    path('categories/<int:category_id>/', views.ProductListByCategoryAPIView.as_view(), name='products_by_category'),
]