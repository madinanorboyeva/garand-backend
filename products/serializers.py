from rest_framework import serializers
from .models import Category, Brand, Product, ProductImage, ProductSpecification, Sale,default_credit_months

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image', 'products_count']
    
    def get_products_count(self, obj):
        return obj.products.count()

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'logo']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_main', 'order']

class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = ['id', 'name', 'value', 'order']

class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    main_image = serializers.SerializerMethodField()
    final_price = serializers.ReadOnlyField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'brand', 'price', 'old_price', 
            'discount_percentage', 'is_on_sale', 'is_credit_available', 
            'is_featured', 'is_bestseller', 'rating', 'main_image', 'final_price'
        ]
    
    def get_main_image(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        if main_image:
            return self.context['request'].build_absolute_uri(main_image.image.url)
        return None

class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    specifications = ProductSpecificationSerializer(many=True, read_only=True)
    final_price = serializers.ReadOnlyField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'brand', 'description', 'price', 
            'old_price', 'discount_percentage', 'is_on_sale', 'is_credit_available',
            'credit_months', 'stock_quantity', 'is_featured', 'is_bestseller', 
            'rating', 'views_count', 'images', 'specifications', 'final_price',
            'created_at', 'updated_at'
        ]

class SaleSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    
    class Meta:
        model = Sale
        fields = ['id', 'product', 'discount_percentage', 'start_date', 'end_date', 'is_active']

class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    credit_months = serializers.JSONField(default=default_credit_months)
    
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_credit_months(self, value):
        if value is None:
            return default_credit_months()
        if not isinstance(value, list):
            raise serializers.ValidationError("credit_months must be a list")
        return value