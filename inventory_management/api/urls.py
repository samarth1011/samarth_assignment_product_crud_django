from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.ApiInfo.as_view(), name='list_all_api'),
    
    path('product/', views.ProductListCreate.as_view(), name='product_view_create'),
    
    path('product/<str:pk>/', views.ProductUpdateDelete.as_view(), name='product_update_delete'),

    path('product_by_id/<str:id>/', views.FindProductById.as_view(), name='product_find_by_id'),

    path('product_by_title/<str:title>/', views.FindProductByTitle.as_view(), name='product_find_by_title'),
    
    path('category/<str:category>/', views.FindProductByCategory.as_view(), name='product_find_by_category'),

    path('product_price_greater_then/<str:price>/', views.FindProductPriceGreaterThan.as_view(), name='product_price_greater_then'),
]