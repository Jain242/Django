
from django.shortcuts import render
from .models import Task, Games
from random import choice


def game(requst):
    game=Games(choice(['head','tail']))
    return render()


# def add_task():
#     tasks=[]
#     for i in range(1,10):

#         task =Task(title=f'name{i}', description=f'description{i}')
#         print(task)
#         tasks.append(task)


# def task_list(request):
#     tasks = add_task()
#     return render(request, 'task.html', {'tasks': tasks})
