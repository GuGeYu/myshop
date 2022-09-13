from django.db import models
from django.urls import reverse
from decimal import Decimal
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='ссылка')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', kwargs={'category_slug': self.slug})


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='brand_imgs/', verbose_name='Изображение')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='ссылка', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def get_absolute_url(self):
        return reverse('product_list_by_brand', kwargs={'brand_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд', null=True)
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='ссылка')
    image = models.ImageField(upload_to='product_imgs/', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Характеристики')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Кол-во на складе')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'id': self.pk, 'slug': self.slug})
