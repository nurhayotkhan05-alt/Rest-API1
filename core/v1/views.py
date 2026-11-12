from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

from rest_framework import mixins, generics



# Create your views here.


@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def product_delete(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response({"message": "Product deleted successfully"}, status=status.HTTP_200_OK)

class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentList(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get(self,request,*args,**kwargs):
        queryset = Student.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,*args,**kwargs):
        return self.destroy(request,pk,*args,**kwargs)

