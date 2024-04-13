from django import forms
from .models import Client, Product, Order

#t=0
#choises = tuple((t,i) for i in Product.objects.all())

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
    
class UserLoginForm(forms.Form):
    login = forms.CharField(label='Lofin', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=30)

class OrderForm(forms.Form):

     client = forms.ModelChoiceField(
         queryset=Client.objects.all()
    
     )
     products =  forms.ModelChoiceField(
         queryset=Product.objects.all()
    
     )

     quanty_products = forms.IntegerField()
    

