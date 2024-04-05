from django.shortcuts import render, get_object_or_404, redirect
from .models import Client,Order, Product
from .forms import ClientForm 
from django.utils import timezone




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

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def view_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'view_client.html', {'client': client})

def update_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form, 'client': client})

def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'delete_client.html', {'client': client})