import datetime 
from django.db import models

class Client(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name,self.email, self.phone_number, self.address,self.registration_date}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quanty_products = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True )



    def __str__(self):
        return f' { self.order_date}'

