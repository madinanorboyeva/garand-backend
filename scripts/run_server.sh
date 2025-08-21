#!/bin/bash

echo "Django serverni ishga tushirish..."

# Virtual environment faollashtirish (agar mavjud bo'lsa)
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Kerakli paketlarni o'rnatish
pip install -r requirements.txt

# Migratsiyalarni yaratish va qo'llash
python manage.py makemigrations
python manage.py migrate

# Superuser yaratish (agar mavjud bo'lmasa)
echo "Superuser yaratish..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser yaratildi: admin/admin123')
else:
    print('Superuser allaqachon mavjud')
"

# Namuna ma'lumotlarni yaratish
python scripts/create_sample_data.py

# Serverni ishga tushirish
echo "Server http://127.0.0.1:8000 da ishga tushmoqda..."
python manage.py runserver
