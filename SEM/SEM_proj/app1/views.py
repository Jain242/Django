from django.shortcuts import render
from .models import Game, Author
from django.http import HttpResponse
import random


def game(request):
    side = random.choice(["orel", "reshka"])
    game = Game(
        side=side,
    )
    game.save()
    return HttpResponse(game)

# Доработаем задачу 1. Добавьте статический метод для статистики по n последним броскам монеты. Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.

def statistics(request):
    n = 9
    last_games = Game.stat_game(n)
    stats = {'orel': 0, 'reshka': 0}

    for game in last_games:
        if game.side == 'orel':
            stats['orel'] += 1
        elif game.side == 'reshka':
            stats['reshka'] += 1
    return HttpResponse(f'{stats} ')


def create_authors(request):
    result = []
    for i in range(10):
        author = Author(name=f'Name{i}', lastname=f'Lastname{i}', email=f'example{i}@mail.ru', biography=f'Biography{i}', birthday=date.today())
        author.save()
        result.append(author.fullname())
    return HttpResponse(f'{result}')