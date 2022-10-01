from django.db import models


class Person(models.Model):
    SHIRT_SIZES = {
        ('S', 'Small'),
        ('M', 'Middle'),
        ('L', 'Large'),
    }
    first_name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
