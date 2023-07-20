from typing import Any

from rest_framework import serializers

from product.models import Products
from tags.serializers import TagsSerializers


class BasketSerializer(serializers.ModelSerializer):
    """Детальная информация о товаре в корзине"""
    count = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    tags = TagsSerializers(many=True, read_only=True)

    class Meta:
        model = Products
        fields = '__all__'

    def get_count(self, obj) -> Any:
        """Переопределяем поле count которое выводит кол-во продукта в корзине, а не в остатках"""
        for item in self.context.get('cart'):  # Бежим по корзине в которой лежат словари из id товара и количества
            if item['id'] == obj.pk:  # Если id товара == id нашего обьекта(Products) то вернем count
                return item['count']

    def get_images(self, obj: {images}) -> list[dict[str, Any]]:
        """Добавляем поле images и по обератной связи получаем все изображения данного продукта"""
        return [
            {
                'src': image.images.url,
                'alt': image.images.name,
            }
            for image in obj.images.all()
        ]

    def get_reviews(self, obj: {reviews}) -> Any:
        """Добавляем поле reviews и считаем по обратной связи общее количество отзывов"""
        return obj.reviews.count()

    def get_rating(self, obj: {reviews}) -> float | int:
        """
        Добавляем поле rating и считаем по обратной связи общее
        количество отзывов, если есть то считаем средний рейтинг продукта
        """
        if obj.reviews.count() > 0:
            res = [o.rate for o in obj.reviews.all()]
            res = sum(res) / len(res)
            return res
        return 0
