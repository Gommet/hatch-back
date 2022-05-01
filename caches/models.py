from django.db import models
from datetime import datetime    

class Session(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField()

class Cache(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    image = models.ImageField(default="llit.jpeg")
    name = models.CharField(max_length=128)
    acomplished = models.BooleanField(default=False)

class Submmit(models.Model):
    cache = models.ForeignKey(Cache, on_delete=models.CASCADE)
    image = models.ImageField(default="llit.jpeg")

class Clue(models.Model):
    cache = models.ForeignKey(Cache, on_delete=models.CASCADE)
    clue = models.TextField()
    datetime = models.DateTimeField(default=datetime.now, blank=True)
