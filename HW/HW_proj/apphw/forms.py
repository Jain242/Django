from django import forms
from .models import Client, Product, Order

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'add_date']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'products', 'total_amount', 'order_date']
