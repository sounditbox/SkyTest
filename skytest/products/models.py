from django.db.models import Model, CharField, CASCADE, BooleanField, \
    DecimalField, ForeignKey, DateField, PositiveIntegerField
from django.utils import timezone


class Category(Model):
    name = CharField("Название категории", max_length=100)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField("Название товара", max_length=255)
    category = ForeignKey(Category, on_delete=CASCADE, verbose_name="Категория")
    is_active = BooleanField("Активен", default=True)
    price = DecimalField("Цена", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(Model):
    product = ForeignKey(Product, on_delete=CASCADE, verbose_name="Товар")
    order_date = DateField("Дата заказа", default=timezone.now)
    quantity = PositiveIntegerField("Количество", default=1)

    def __str__(self):
        return f"Заказ для {self.product.name} от {self.order_date}"
