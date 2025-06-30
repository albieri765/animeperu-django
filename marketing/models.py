from django.db import models

class ContestEntry(models.Model):
    email     = models.EmailField(unique=True)
    nombre    = models.CharField(max_length=100)
    anime_fav = models.CharField(max_length=100)
    creado    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email