from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.ApiInfo.as_view(), name='list_all_api'),
    
    path('products/', views.ProductListCreate.as_view(), name='product_view_create'),
    
    path('products/<str:pk>/', views.ProductUpdateDelete.as_view(), name='product_update_delete'),

    path('products_by_id/<str:id>/', views.FindProductById.as_view(), name='product_find_by_id'),

    path('products_by_title/<str:title>/', views.FindProductByTitle.as_view(), name='product_find_by_title'),
    
    path('categorys/<str:category>/', views.FindProductByCategory.as_view(), name='product_find_by_category'),

    path('products_price_greater_then/<str:price>/', views.FindProductPriceGreaterThan.as_view(), name='product_price_greater_then'),
]