from rest_framework import serializers

from store.models import Product



class ProductSerializer(serializers.ModelSerializer):
    # def get_choices():
    # # Example logic to get choices dynamically
    #     return [(product.id, product.name) for product in Product.objects.all()]

    # # Example field using dynamic choices
    # product_choices = serializers.ChoiceField(choices=get_choices())
    class Meta:
        model = Product
        fields = ('name','price',)

class listserializer(serializers.ListSerializer):
    child = ProductSerializer()
# class SaleSerializer(serializers.ModelSerializer):
#     class Meta:
        