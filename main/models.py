from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=100,verbose_name='Слаг', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def get_absolute_url(self):
        return reverse("main:product_list_by_category", args=[self.slug])

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Продукты')
    name = models.CharField(max_length=100, verbose_name='Название продукта', db_index=True)
    slug = models.SlugField(max_length=100, verbose_name='Слаг', unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    available = models.BooleanField(default=True)
    created =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (
            'name',
        )

    def get_absolute_url(self):
        return reverse("main:product_detail", args=[self.id,self.slug])

    def __str__(self):
        return self.name

  

  