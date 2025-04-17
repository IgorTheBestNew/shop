import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from shop.models import Category, Product

# Створимо категорію, якщо не існує
category, created = Category.objects.get_or_create(
    name="Електроніка",
    slug="elektronika"
)

# Приклади назв товарів
product_names = [
    "Смартгодинник Q88",
    "Навушники Sonic Boom",
    "Портативна колонка MiniBass",
    "Зарядний пристрій 20W",
    "Кабель USB-C",
    "Геймерська мишка Hyper",
    "Клавіатура RGB Max",
    "Екран захисту для телефону",
    "Bluetooth трекер",
    "Wi-Fi адаптер"
]

for name in product_names:
    product, created = Product.objects.get_or_create(
        name=name,
        slug=name.lower().replace(" ", "-"),
        category=category,
        defaults={
            "description": f"Опис для {name}.",
            "price": round(random.uniform(99, 999), 2),
            "stock": random.randint(5, 100),
            "available": True,
        }
    )
    if created:
        print(f"✅ Додано: {name}")
    else:
        print(f"ℹ️ Вже існує: {name}")
