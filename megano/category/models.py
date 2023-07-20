from django.db import models


class Category(models.Model):
    """
    Модель категории
    """
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Изображение', upload_to='catalog_images')

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    """
    Модель подкатегории, связь ForeignKey с Category
    """
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Изображение', upload_to='subcategories_images')
    subcategories = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT,
                                      related_name='subcategories')

    def __str__(self):
        return self.title
