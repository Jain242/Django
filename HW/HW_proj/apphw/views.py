from django.shortcuts import render, get_object_or_404, redirect
from .models import Client,Order, Product
from .forms import ClientForm,ProductForm, OrderForm, UserLoginForm
from django.utils import timezone
from faker import Faker
from django.core.files.storage import FileSystemStorage
from random import randint
from django.contrib.auth import authenticate, login

fake = Faker()


def ordered_products(request, client_id, period):
    client_orders = Order.objects.filter(client_id=client_id, order_date__gte=get_period_start_date(period))
    products = Product.objects.filter(order__in=client_orders).distinct().order_by('added_date')
    return render(request, 'ordered_products.html', {'products': products})

def get_period_start_date(period):
    today = timezone.now().date()
    if period == 'week':
        return today - timezone.timedelta(days=7)
    elif period == 'month':
        return today - timezone.timedelta(days=30)
    elif period == 'year':
        return today - timezone.timedelta(days=365)
    else:
        return today

def make_order(request):
    form = {'Вы вошли'}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']

            products = form.cleaned_data['products']
            print(products.price)
            quanty_products = form.cleaned_data['quanty_products']
            order = Order(client = client, products = products,quanty_products=quanty_products,total_amount = products.price*quanty_products)
           
            order.save()
            redirect('client_list' )
        else:
            form = OrderForm()
    return render(request, 'make_order.html',{'form': form})

def update_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            fs = FileSystemStorage()
            fs.save(client)
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form, 'client': client})


def create_client(request,count):
    clients = []
    for i in range(count):
        client = Client(login = fake.first_name()+ str(randint(1,100)),password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True),name = fake.name(), email = fake.email(),phone_number = fake.phone_number(), address = fake.address())
        clients.append(client)
        
        client.save()
    return render(request, 'create_client.html', {'count': count})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def view_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'view_client.html', {'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'delete_client.html', {'client': client})


def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})




def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            product = Product(name = name,description = description, price=price,quantity=quantity ,image=f'{image.name}')
            product.save()
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ProductForm()
    return render(request, 'input_image.html', {'form' : form})

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            client = Client.objects.filter(login = login,password = password)
            if client:
                 return redirect('make_order')
            else:
                error_message = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})