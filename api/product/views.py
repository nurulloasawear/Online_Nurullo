from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from .serializers import ProductMultySerializer as ProductSerializer

@api_view(['GET', 'POST'])
def product_con_img(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def product_detail(request, pk):
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response({'error': 'Product not found'}, status=404)

#     serializer = ProductSerializer(product)
#     return Response(serializer.data)
	pass