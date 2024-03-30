from django.db import models

# Create your models here.


class Game(models.Model):
    side = models.CharField(max_length=10)
    time_res = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.side}, time = {self.time_res}"
    
    @staticmethod
    def stat_game(n):
        return Game.objects.all().order_by('-time_res')[:n]