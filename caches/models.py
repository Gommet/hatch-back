from django.db import models

class Session(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField()

class Cache(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    acomplished = models.BooleanField(default=False)

class Clue(models.Model):
    cache = models.ForeignKey(Cache, on_delete=models.CASCADE)
    clue = models.TextField()
