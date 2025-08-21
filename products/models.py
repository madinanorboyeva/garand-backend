from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


def default_credit_months():
    return [3, 6, 12, 24]

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name="Tavsif")
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['name']
    
    def __str__(self):
        return self.nameven 

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Brend nomi")
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Mahsulot nomi")
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(verbose_name="Tavsif")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narx")
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Eski narx")
    discount_percentage = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Chegirma foizi"
    )
    is_on_sale = models.BooleanField(default=False, verbose_name="Chegirmada")
    is_credit_available = models.BooleanField(default=True, verbose_name="Kreditga")
    credit_months = models.JSONField(default=default_credit_months, verbose_name="Kredit muddatlari")
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Ombordagi miqdor")
    is_featured = models.BooleanField(default=False, verbose_name="Tavsiya etiladi")
    is_bestseller = models.BooleanField(default=False, verbose_name="Eng ko'p sotilgan")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    

    @property
    def final_price(self):
        if self.old_price and self.discount_percentage > 0:
            return self.old_price * (Decimal(1) - Decimal(self.discount_percentage) / Decimal(100))
        return self.price


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    is_main = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.product.name} - Image {self.order}"

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    name = models.CharField(max_length=100, verbose_name="Xususiyat nomi")
    value = models.CharField(max_length=200, verbose_name="Qiymati")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.product.name} - {self.name}: {self.value}"

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    discount_percentage = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(90)])
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Chegirma"
        verbose_name_plural = "Chegirmalar"
    
    def __str__(self):
        return f"{self.product.name} - {self.discount_percentage}%"