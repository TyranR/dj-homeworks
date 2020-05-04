from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=10, unique=True)
    # prepopulated_fields = {"slug": ("name",)}

    def __str__(self):
        return self.name
