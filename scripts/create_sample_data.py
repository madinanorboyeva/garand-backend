import os
import sys
import django

# Django sozlamalarini yuklash
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'garand_backend.settings')
django.setup()

from products.models import Category, Brand, Product, ProductImage, ProductSpecification, Sale
from django.utils.text import slugify
from datetime import datetime, timedelta

def create_sample_data():
    print("Namuna ma'lumotlarni yaratish boshlandi...")
    
    # Kategoriyalar yaratish
    categories_data = [
        {'name': 'Xolodilnik', 'description': 'Turli xil xolodilniklar'},
        {'name': 'Kir yuvish mashinasi', 'description': 'Avtomatik kir yuvish mashinalari'},
        {'name': 'Televizor', 'description': 'Smart va oddiy televizorlar'},
        {'name': 'Konditsioner', 'description': 'Split va mobil konditsionerlar'},
        {'name': 'Mikroto\'lqinli pech', 'description': 'Turli hajmdagi mikroto\'lqinli pechlar'},
        {'name': 'Changyutgich', 'description': 'Robot va oddiy changyutgichlar'},
    ]
    
    categories = []
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'slug': slugify(cat_data['name']),
                'description': cat_data['description']
            }
        )
        categories.append(category)
        if created:
            print(f"Kategoriya yaratildi: {category.name}")
    
    # Brendlar yaratish
    brands_data = ['Samsung', 'LG', 'Artel', 'Shivaki', 'Bosch', 'Electrolux', 'Haier', 'Midea']
    
    brands = []
    for brand_name in brands_data:
        brand, created = Brand.objects.get_or_create(name=brand_name)
        brands.append(brand)
        if created:
            print(f"Brend yaratildi: {brand.name}")
    
    # Mahsulotlar yaratish
    products_data = [
        {
            'name': 'Samsung RB37J5000SA Xolodilnik',
            'category': 'Xolodilnik',
            'brand': 'Samsung',
            'description': 'Zamonaviy dizayn va yuqori sifatli Samsung xolodilnigi. No Frost texnologiyasi bilan.',
            'price': 4500000,
            'old_price': 5000000,
            'discount_percentage': 10,
            'is_on_sale': True,
            'is_featured': True,
            'is_bestseller': True,
            'credit_months': [3, 6, 12, 24],
            'stock_quantity': 15,
            'specifications': [
                {'name': 'Hajmi', 'value': '367 litr'},
                {'name': 'Energiya sinfi', 'value': 'A++'},
                {'name': 'Rang', 'value': 'Kumush'},
                {'name': 'No Frost', 'value': 'Ha'},
            ]
        },
        {
            'name': 'LG F4V5RGP2T Kir yuvish mashinasi',
            'category': 'Kir yuvish mashinasi',
            'brand': 'LG',
            'description': 'AI Direct Drive texnologiyasi bilan jihozlangan zamonaviy kir yuvish mashinasi.',
            'price': 6200000,
            'old_price': 6800000,
            'discount_percentage': 9,
            'is_on_sale': True,
            'is_featured': True,
            'credit_months': [6, 12, 24],
            'stock_quantity': 8,
            'specifications': [
                {'name': 'Yuklash hajmi', 'value': '9 kg'},
                {'name': 'Energiya sinfi', 'value': 'A+++'},
                {'name': 'Aylanish tezligi', 'value': '1400 ayl/daq'},
                {'name': 'Smart Diagnosis', 'value': 'Ha'},
            ]
        },
        {
            'name': 'Samsung UE55AU7100 Smart TV',
            'category': 'Televizor',
            'brand': 'Samsung',
            'description': '55 dyuymli 4K UHD Smart televizor. Crystal UHD texnologiyasi bilan.',
            'price': 7500000,
            'is_featured': True,
            'is_bestseller': True,
            'credit_months': [6, 12, 18, 24],
            'stock_quantity': 12,
            'specifications': [
                {'name': 'Ekran o\'lchami', 'value': '55 dyuym'},
                {'name': 'Ruxsat', 'value': '4K UHD (3840x2160)'},
                {'name': 'Smart TV', 'value': 'Tizen OS'},
                {'name': 'HDR', 'value': 'HDR10+'},
            ]
        },
        {
            'name': 'Artel ART-09HRN Konditsioner',
            'category': 'Konditsioner',
            'brand': 'Artel',
            'description': 'Inverter texnologiyali split konditsioner. Energiya tejamkor va shovqinsiz.',
            'price': 3200000,
            'old_price': 3600000,
            'discount_percentage': 11,
            'is_on_sale': True,
            'credit_months': [3, 6, 12],
            'stock_quantity': 20,
            'specifications': [
                {'name': 'Sovutish quvvati', 'value': '9000 BTU'},
                {'name': 'Energiya sinfi', 'value': 'A++'},
                {'name': 'Inverter', 'value': 'Ha'},
                {'name': 'Xona hajmi', 'value': '25-30 m²'},
            ]
        },
        {
            'name': 'Bosch HMT75M654 Mikroto\'lqinli pech',
            'category': 'Mikroto\'lqinli pech',
            'brand': 'Bosch',
            'description': 'Ko\'mma mikroto\'lqinli pech. Gril va konveksiya funksiyalari bilan.',
            'price': 2800000,
            'is_featured': True,
            'credit_months': [3, 6, 12],
            'stock_quantity': 10,
            'specifications': [
                {'name': 'Hajmi', 'value': '20 litr'},
                {'name': 'Quvvat', 'value': '800 Vt'},
                {'name': 'Gril', 'value': 'Ha'},
                {'name': 'Konveksiya', 'value': 'Ha'},
            ]
        },
        {
            'name': 'Electrolux PURE i9.2 Robot changyutgich',
            'category': 'Changyutgich',
            'brand': 'Electrolux',
            'description': 'Aqlli robot changyutgich. 3D Vision texnologiyasi bilan.',
            'price': 4800000,
            'old_price': 5200000,
            'discount_percentage': 8,
            'is_on_sale': True,
            'is_bestseller': True,
            'credit_months': [6, 12, 18],
            'stock_quantity': 6,
            'specifications': [
                {'name': 'Batareya', 'value': '3400 mAh'},
                {'name': 'Ish vaqti', 'value': '60 daqiqa'},
                {'name': '3D Vision', 'value': 'Ha'},
                {'name': 'Wi-Fi', 'value': 'Ha'},
            ]
        },
    ]
    
    for product_data in products_data:
        category = Category.objects.get(name=product_data['category'])
        brand = Brand.objects.get(name=product_data['brand'])
        
        product, created = Product.objects.get_or_create(
            name=product_data['name'],
            defaults={
                'slug': slugify(product_data['name']),
                'category': category,
                'brand': brand,
                'description': product_data['description'],
                'price': product_data['price'],
                'old_price': product_data.get('old_price'),
                'discount_percentage': product_data.get('discount_percentage', 0),
                'is_on_sale': product_data.get('is_on_sale', False),
                'is_featured': product_data.get('is_featured', False),
                'is_bestseller': product_data.get('is_bestseller', False),
                'credit_months': product_data.get('credit_months', []),
                'stock_quantity': product_data.get('stock_quantity', 0),
                'rating': 4.5,
            }
        )
        
        if created:
            print(f"Mahsulot yaratildi: {product.name}")
            
            # Texnik xususiyatlarni qo'shish
            for i, spec in enumerate(product_data.get('specifications', [])):
                ProductSpecification.objects.create(
                    product=product,
                    name=spec['name'],
                    value=spec['value'],
                    order=i
                )
    
    # Chegirmalar yaratish
    sale_products = Product.objects.filter(is_on_sale=True)
    for product in sale_products:
        Sale.objects.get_or_create(
            product=product,
            defaults={
                'discount_percentage': product.discount_percentage,
                'start_date': datetime.now() - timedelta(days=5),
                'end_date': datetime.now() + timedelta(days=25),
                'is_active': True
            }
        )
    
    print("Namuna ma'lumotlar muvaffaqiyatli yaratildi!")

if __name__ == '__main__':
    create_sample_data()
