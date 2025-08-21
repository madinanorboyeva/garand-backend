from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Kutilmoqda'),
        ('confirmed', 'Tasdiqlangan'),
        ('processing', 'Jarayonda'),
        ('shipped', 'Yuborilgan'),
        ('delivered', 'Yetkazilgan'),
        ('cancelled', 'Bekor qilingan'),
    ]
    
    PAYMENT_CHOICES = [
        ('cash', 'Naqd'),
        ('card', 'Karta'),
        ('credit', 'Kredit'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    first_name = models.CharField(max_length=50, verbose_name="Ism")
    last_name = models.CharField(max_length=50, verbose_name="Familiya")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(blank=True, verbose_name="Email")
    address = models.TextField(verbose_name="Manzil")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='cash')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Umumiy summa")
    notes = models.TextField(blank=True, verbose_name="Izohlar")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Buyurtma #{self.id} - {self.first_name} {self.last_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Buyurtma elementi"
        verbose_name_plural = "Buyurtma elementlari"
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
    @property
    def total_price(self):
        return self.price * self.quantity

class CreditApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ko\'rib chiqilmoqda'),
        ('approved', 'Tasdiqlangan'),
        ('rejected', 'Rad etilgan'),
    ]
    
    first_name = models.CharField(max_length=50, verbose_name="Ism")
    last_name = models.CharField(max_length=50, verbose_name="Familiya")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    passport_series = models.CharField(max_length=10, verbose_name="Pasport seriyasi")
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Oylik daromad")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    credit_months = models.IntegerField(verbose_name="Kredit muddati (oy)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Kredit arizasi"
        verbose_name_plural = "Kredit arizalari"
    
    def __str__(self):
        return f"Kredit arizasi - {self.first_name} {self.last_name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    subject = models.CharField(max_length=200, verbose_name="Mavzu")
    message = models.TextField(verbose_name="Xabar")
    is_read = models.BooleanField(default=False, verbose_name="O'qilgan")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Aloqa xabari"
        verbose_name_plural = "Aloqa xabarlari"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
