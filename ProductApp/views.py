from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Product
from .serializers import ProductSerializer


class ProductListHandler(APIView):

    def __init__(self):
        self.queryset = Product.objects.all()
        self.filter_backends = (DjangoFilterBackend,)
        self.filter_fields = ('name','category',)

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self,request):
        queryset = self.filter_queryset(self.queryset)
        serializer = ProductSerializer(queryset,many = True)
        return Response(serializer.data)

    def post(self,request):
        data = self.request.data
        try:
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                result = serializer.create(serializer.validated_data)
                return Response({"results":ProductSerializer(result).data})
            raise(ValidationError(serializer.errors))
        except ValidationError as err:
            content = {"errors":err.message_dict}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductHandler(APIView):

    def __init__(self):
        self.queryset = Product.objects.all()

    def get(self,request,pk):
        try:
            queryset = Product.objects.get(id = pk)
            serializer = ProductSerializer(queryset)
            return Response(serializer.data)
        except ObjectDoesNotExist as err:
            content = {"errors":"Product with id "+ str(pk) + " does not exist!!" }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk):
        data = self.request.data
        try:
            prod_obj = Product.objects.get(id = pk)
            serializer = ProductSerializer(prod_obj,data=data,partial=True)
            if serializer.is_valid():
                result = serializer.save()
                return Response({"results":ProductSerializer(result).data})
            else: raise(ValidationError(serializer.errors))
        except ObjectDoesNotExist as err:
            content = {"errors":err}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as err:
            content = {"errors":err.message_dict}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request,pk):
        try:
            prod_obj = Product.objects.get(id=pk)
            prod_obj.delete()
            return Response({"results":"Successfully Deleted the data"})
        except ObjectDoesNotExist as err:
            content = {"errors":"Product with id "+ str(pk) + " does not exist!!" }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

