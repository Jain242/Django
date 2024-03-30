from django.urls import path
from . import views

urlpatterns = [
    path('game', views.game, name='game'),
    path('statistics', views.statistics, name='statistics'),
]
