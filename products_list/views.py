from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"message": "All Products",
                         "payload": serializer.data}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Product Created",
                         "payload": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response({"message": "Product Retrieved",
                         "payload": serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Product Updated",
                         "payload": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        Product.delete(product)
        return Response({"message": "Product Deleted",
                         "payload": None}, status=status.HTTP_204_NO_CONTENT)
