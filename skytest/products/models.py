import calendar
from datetime import date, timedelta

from django.db.models import Model, CharField, CASCADE, BooleanField, \
    DecimalField, ForeignKey, DateField, PositiveIntegerField, Sum
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

    def orders_sum_by_month(self, month: int = None, year: int = None) -> int:
        """
        Вычисляет сумму заказов (количество) для указанного месяца и года.
        По умолчанию используются текущий месяц и год.
        Используется __range, а не __month, чтобы запрос в БД был через BETWEEN,
        а не через EXTRACT, что позволит воспользоваться индексом по дате
        """

        today = timezone.now().date()
        year = year or today.year
        month = month or today.month
        if not (1 <= month <= 12):
            raise ValueError("Месяц должен быть в диапазоне от 1 до 12.")

        first_day = date(year, month, 1)
        last_day = date(year, month, calendar.monthrange(year, month)[1])

        orders = self.order_set.filter(order_date__range=[first_day, last_day])
        total = orders.aggregate(total=Sum('quantity'))['total']
        return total or 0

    def orders_last_month(self):
        today = timezone.now().date()
        last_day = today.replace(day=1) - timedelta(days=1)
        return self.orders_sum_by_month(last_day.month, last_day.year)

    def orders_current_month(self):
        return self.orders_sum_by_month()

    def __str__(self):
        return self.name


class Order(Model):
    product = ForeignKey(Product, on_delete=CASCADE, verbose_name="Товар")
    order_date = DateField("Дата заказа", default=timezone.now)
    quantity = PositiveIntegerField("Количество", default=1)

    def __str__(self):
        return f"Заказ для {self.product.name} от {self.order_date}"
