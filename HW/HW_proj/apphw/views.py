from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger('django')



def index(request):
    html = """
    <html>
    <head><title>Главная страница</title></head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    </body>
    </html>
    """

    log_data = f"VISIT MAIN PAGE IP: {request.META.get('REMOTE_ADDR')}, User-Agent: {request.META.get('HTTP_USER_AGENT')}"
    logger.info(log_data) 
    return HttpResponse(html)


def about(request):
    html = """
    <html>
    <head><title>О себе</title></head>
    <body>
        <h1>Обо мне</h1>
        <p>Привет! Это мой сайт на Django.</p>
  
    </body>
    </html>
    """
    log_data = f"VISIT ABOUT PAGE. IP: {request.META.get('REMOTE_ADDR')}, User-Agent: {request.META.get('HTTP_USER_AGENT')}"
    logger.info(log_data)  

    return HttpResponse(html)
