from distutils.command.upload import upload
from email.policy import default
from turtle import title
from django.db import models
from django.db.models.fields.files import ImageField


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(
        'categories.category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
