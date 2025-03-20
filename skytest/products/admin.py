from django.contrib import admin

from .models import Category, Product, Order

admin.site.site_title = "Административная панель сайта"
admin.site.site_header = "Панель управления сайтом"
admin.site.index_title = "Добро пожаловать в админку"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "is_active", "price")
    list_filter = ("is_active", "category")
    search_fields = ("name",)
    fieldsets = (
        (None, {"fields": ("name", "category", "is_active", "price")}),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "order_date", "quantity")
    list_filter = ("order_date", "product")
    date_hierarchy = "order_date"
    search_fields = ("product__name",)
