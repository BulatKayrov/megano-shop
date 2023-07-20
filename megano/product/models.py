from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg

from category.models import Category
from tags.models import Tags


class Specification(models.Model):
    """Модель спецификаций"""
    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'

    name = models.CharField(max_length=200)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Products(models.Model):
    """Модель товаров"""
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    category = models.ForeignKey(Category, verbose_name='Категория ',on_delete=models.PROTECT, related_name='product_category')
    price = models.DecimalField('Цена', max_digits=15, decimal_places=2)
    count = models.PositiveIntegerField('Кол-во товаров',default=0)
    date = models.DateTimeField('Дата создания',auto_now_add=True)
    title = models.CharField('Название',max_length=200)
    description = models.TextField('Краткое описание',blank=True)
    fullDescription = models.TextField('Полное описание',blank=True)
    freeDelivery = models.BooleanField('Бесплатная доставка',default=True, blank=True)
    tags = models.ManyToManyField(Tags, verbose_name='Теги', related_name='tags', blank=True)
    popular = models.BooleanField('Популярный', default=False)
    limited = models.BooleanField('Лимитированный',default=False)
    dateFrom = models.DateTimeField('Дата начала',blank=True, null=True)
    dateTo = models.DateTimeField('Дата окончания',blank=True, null=True)
    salePrice = models.DecimalField('Цена со скидкой',max_digits=15, decimal_places=2, blank=True, null=True)
    sale = models.BooleanField('Скидка',default=False)
    specification = models.ForeignKey(Specification, verbose_name='Спецификация', on_delete=models.PROTECT, related_name='specification')

    def review_count(self):
        return self.reviews.count()

    def rating(self):
        return self.reviews.aggregate(Avg('rate'))['rate__avg']

    def __str__(self):
        return f'{self.title}'


class ProductImage(models.Model):
    """Модель изображений товара"""
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображении'

    images = models.ImageField('Фотография',upload_to='products_images', blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.product.title}'


class Review(models.Model):
    """Модель отзывов"""
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    RATING = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(null=True, blank=True)
    rate = models.PositiveSmallIntegerField(blank=True, choices=RATING)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Автор: {self.author.username} Оценка: {self.rate} Текст: {self.text[:50]}'
