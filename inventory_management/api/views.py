# Create your views here.
from django.urls import reverse
from rest_framework.response import Response
from .models import Product
from rest_framework import generics,status
from .serializers import  ProductSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
# Add or List Products
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        product_name = serializer.validated_data.get('name')
        if Product.objects.filter(name=product_name).exists():
           raise APIException("A product with this name already exists.")
            
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    # Delete all Products
    def delete(self):
        Product.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Update or Delete Product by ID
class ProductUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        product_name = serializer.validated_data.get('name')
        product_id = self.get_object().id
        if Product.objects.filter(name=product_name).exclude(id=product_id).exists():
           raise APIException("A product with this name already exists.")
            
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

# Find Product by name
class FindProductByTitle(APIView):
    def get(self, request, *args, **kwargs):
        # Get the tile from query parameter
        title = kwargs.get('title')  
        
        try:
            products = Product.objects.filter(name__icontains = title)
            if products.count()==0:raise Exception()
        except Exception as e:
            raise APIException(f"Product with title {title} not found", code=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
 
# Find Product by category name   
class FindProductByCategory(APIView):
    def get(self, request, *args, **kwargs):
        # Get the tile from query parameter
        try:
            category = kwargs.get('category')
            
            products = Product.objects.filter(category__icontains = category)
            if products.count()==0:raise Exception
        except Exception as e:
            raise APIException(f"Product with category name {category} not found", code=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        

# Find Product by whose price greater then:
class FindProductPriceGreaterThan(APIView):
    def get(self, request, *args, **kwargs):
        # Get the tile from query parameter
        try:
            price = kwargs.get('price')  
        
            products = Product.objects.filter(price__gt=price)
        except Exception as e:
            raise APIException("Check the price format you have provided", e)
        
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



# Find Product by category name   
class FindProductById(APIView):
    def get(self, request, *args, **kwargs):
        # Get the tile from query parameter
        try:
            id = kwargs.get('id')
        
            # retrieve the product by ID
            product = Product.objects.get(id = id)
        except Exception as e:
            raise APIException(f"Product with id {id} not found.", code=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ApiInfo(APIView):
    def get(self, request, *args, **kwargs):
        # Hard-coded list of API endpoints and their information
        api_info = [

            {
                'url': reverse('product_view_create'),
               
                'description': 'View and create products, Delete all Products'
            },
            {
                'url': reverse('product_update_delete', kwargs={'pk': 1}),
                
                'description': 'Update or delete a product by ID.'
            },
            {
                'url': reverse('product_find_by_id', kwargs={'id': 1}),
                
                'description': 'Find Product by ID.'
            },
            {
                'url': reverse('product_find_by_title', kwargs={'title': 'saree'}),
                
                'description': 'Find product by title.'
            },
            {
                'url': reverse('product_find_by_category', kwargs={'category': 'men'}),
                
                'description': 'Find product by category.'
            },
            {
                'url': reverse('product_price_greater_then', kwargs={'price': 399}),
                
                'description': 'Find products with price greater than the specified value.'
            }
        ]
        return Response(data=api_info, status=status.HTTP_200_OK)

