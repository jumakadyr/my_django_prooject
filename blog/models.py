from django.db import models

class Phone (models.Model):
    brand = models.CharField(max_length=55)
    model = models.CharField(max_length=55)
    price = models.IntegerField()

