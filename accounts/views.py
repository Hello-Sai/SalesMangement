from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,GenericAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from accounts.models import Customer, Employee
from accounts.serializer import CustomerSerializer, EmployeeSerializer

# Create your views here.
class LoginView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = EmployeeSerializer
    def post(self,request):
        account = authenticate(username = request.data['username'],password = request.data['password'])
        if account:
            token = RefreshToken.for_user(account)
            return Response({'refresh':str(token),'access':str(token.access_token)})
        return Response({'error':"Invalid Username/Password"},status=400)

class EmployeeView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

class CustomerView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'


