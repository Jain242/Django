from django.contrib import admin
from .models import Client, Product, Order

# Административный класс для модели Client
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']  # Какие поля отображать в списке объектов

# Административный класс для модели Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity']  # Какие поля отображать в списке объектов

# Административный класс для модели Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date']  # Какие поля отображать в списке объектов

# Регистрация административных классов
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)