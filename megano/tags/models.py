from django.db import models


class Tags(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
