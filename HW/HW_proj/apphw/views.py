from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
#from .forms import ClientForm 


# logger = logging.getLogger('django')



# def index(request):
#     html = """
#     <html>
#     <head><title>Главная страница</title></head>
#     <body>
#         <h1>Добро пожаловать на мой первый Django-сайт!</h1>
#     </body>
#     </html>
#     """

#     log_data = f"VISIT MAIN PAGE IP: {request.META.get('REMOTE_ADDR')}, User-Agent: {request.META.get('HTTP_USER_AGENT')}"
#     logger.info(log_data) 
#     return HttpResponse(html)


# def about(request):
#     html = """
#     <html>
#     <head><title>О себе</title></head>
#     <body>
#         <h1>Обо мне</h1>
#         <p>Привет! Это мой сайт на Django.</p>
  
#     </body>
#     </html>
#     """
#     log_data = f"VISIT ABOUT PAGE. IP: {request.META.get('REMOTE_ADDR')}, User-Agent: {request.META.get('HTTP_USER_AGENT')}"
#     logger.info(log_data)  

#     return HttpResponse(html)




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