from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 64, unique = False)
    nick = models.CharField(max_length = 64, unique = False)
    email = models.EmailField(max_length = 128, unique = True)

    def __str__(self):
        return self.nick