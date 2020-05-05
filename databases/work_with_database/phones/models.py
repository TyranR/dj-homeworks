from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=32)
    price = models.DecimalField(verbose_name='Цена', max_digits=6, decimal_places=0)
    image = models.CharField(verbose_name='Картинка', max_length=128)
    release_date = models.DateField(verbose_name='Дата')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(verbose_name='Slugify URL', max_length=10, unique=True)

    def __str__(self):
        return self.title

    def sluggg(self):
        return slugify(self.title)
