from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Harga harus lebih besar dari 0")
        return value
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Nama produk minimal 3 karakter")
        return value