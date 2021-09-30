from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,unique=True)
    description = models.TextField()
    units = models.IntegerField()
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.name

