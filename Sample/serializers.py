from rest_framework import serializers
from .models import Companies, Product, Purchase_Order


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('id', 'Name', 'GST')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'Name', 'Company', 'Cost')


class Purchase_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Order
        fields = ('Purchase_Order_Number', 'Company', 'Product_Name', 'Rate', 'Quantity', 'Total_Price')
