
# Create your models here.
from django.db import models

# class Task(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
    
class Games(models.Model):
    side = models.CharField(max_length=100)
    time_res = models.DateTimeField(auto_now_add=True)
