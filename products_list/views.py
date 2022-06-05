import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"status": "success",
                         "data": {"products": serializer.data}}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "success",
                         "data": {"product": serializer.data}}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response({"status": "success",
                         "data": {"product": serializer.data}}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "success",
                         "data": {"product": serializer.data}}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        Product.delete(product)
        return Response({"status": "success",
                         "data": None}, status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            "status": "success",
            "data": {"id": user.id}
        }, status=status.HTTP_200_OK)
