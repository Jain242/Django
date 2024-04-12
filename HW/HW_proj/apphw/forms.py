from django import forms
from .models import Client, Product, Order

class ClientForm(forms.Form):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number', 'address']

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField(min_value=0)
    image = forms.ImageField()
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'products', 'total_amount']

