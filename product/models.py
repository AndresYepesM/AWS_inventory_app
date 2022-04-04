from django.db import models
from django.urls import reverse_lazy
from PIL import Image

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length = 35, verbose_name='Item name')
    img = models.ImageField(upload_to='static/img/upload/product', blank=True)
    price =  models.IntegerField( blank=True)
    detail = models.TextField( blank=True)
    quantity = models.IntegerField( blank=True)
    class Meta:
        ordering=['id']
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.id}.)   {self.name}'

    def get_absolute_url(self):
        return reverse_lazy('Product:form_success')