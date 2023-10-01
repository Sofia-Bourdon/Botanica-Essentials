from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sku = models.CharField(max_length=255, unique=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)  # Change here

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
