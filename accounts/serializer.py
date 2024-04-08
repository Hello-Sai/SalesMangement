from rest_framework import serializers
from store.serializers import ProductSerializer
from accounts.models import Customer, Employee
from store.models import Product
# from store.serializers import ProductSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('username','password',)

    def create(self, validated_data):
        return Employee.objects.create_user(**validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    products =serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),many=True,)
    class Meta:
        model = Customer
        fields = '__all__'
    
    def create(self, validated_data):
        super().create(validated_data)
        return [getattr('id',data) for data in validated_data.pop('products')]
    