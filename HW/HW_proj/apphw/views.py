from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger('django')


# Create your views here.
# Представление для главной страницы
def index(request):
    html = """
    <html>
    <head><title>Главная страница</title></head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
        <p>Здесь вы найдете информацию о моем первом Django-приложении и обо мне.</p>
    </body>
    </html>
    """
    # Сохранение данных о посещении страницы в логи
    log_data = f"Посещена главная страница. IP: {request.META.get('REMOTE_ADDR')}, User-Agent: {request.META.get('HTTP_USER_AGENT')}"
    logger.info(log_data)  # Записываем информацию в лог

    return HttpResponse(html)

# Представление для страницы "О себе"
def about(request):
    html = """
    <html>
    <head><title>О себе</title></head>
    <body>
        <h1>Обо мне</h1>
        <p>Привет! Я создал этот сайт с помощью Django.</p>
        <p>Меня зовут , и я начинающий разработчик.</p>
    </body>
    </html>
    """
    log_data = f"Посещена страница 'О себе'. IP: {request.META.get('REMOTE_ADDR')}, User-Agent: {request.META.get('HTTP_USER_AGENT')}"
    logger.info(log_data)  

    return HttpResponse(html)
