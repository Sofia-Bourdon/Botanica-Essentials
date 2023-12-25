from django.db import models
from django.utils.text import slugify
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name="products")
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sku = models.CharField(max_length=255, unique=True)
    image = cloudinary.models.CloudinaryField('image', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
