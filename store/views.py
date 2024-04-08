from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from accounts.models import Employee,Customer
from accounts.serializer import CustomerSerializer, EmployeeSerializer
from django.db.models import Count
from store.models import Product
from store.serializers import ProductSerializer
# Create your views here.
from rest_framework.response import Response

class ProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name'
    

class SalesView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        print(serializer.data)
        products = Product.objects.filter(id__in = serializer.data.pop('products'))
        self.request.user.sale(products)
        try:
            self.create(serializer.data)
            return Response('Successfully saved')
        except Exception as e:
            return Response({'error':e},status=400)
        
class AnalysisView(ListAPIView):
    serializer_class = ProductSerializer
    def list(self, request, *args, **kwargs):
        object = Employee.objects.all().order_by('-sales').first()
        product = Product.objects.all().order_by('-sales').first()
        # objserializer = EmployeeSerializer(object)
        # qsetserializer = ProductSerializer(queryset)
        if not object.sales ==0:
            return Response({'employee':f'{object.username} has highest sales {object.sales}','products':f'{product.name} has High Sales {product.sales}'})
        return Response('Sales Not Yet Started')
        #  Category.objects.annotate(product_count=Count('product')).aggregate(max_count=Max('product_count'))