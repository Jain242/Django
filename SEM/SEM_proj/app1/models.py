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
    

    class Author(models.Model):
        name = models.CharField(max_length=100)
        lastname = models.CharField(max_length=100)
        email = models.EmailField()
        biography = models.TextField(max_length=1500)
        birthday = models.DateField(blank=False)

        def fullname(self):
            return f'{self.name} {self.lastname}'