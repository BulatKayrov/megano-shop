from typing import Any
from rest_framework import serializers
from product.models import Specification, Products, Review


class SpecificationSerializers(serializers.ModelSerializer):
    """Сериализации данных из модели Specification"""
    class Meta:
        model = Specification
        fields = ['name', 'value']


class ProductSerializers(serializers.ModelSerializer):
    """Сериализации данных из модели Products"""
    class Meta:
        model = Products
        fields = [
            'id', 'category', 'price', 'count', 'date', 'title', 'description', 'fullDescription',
            'freeDelivery', 'images', 'tags', 'specification', 'rating', 'reviews'
        ]

    images = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    specification = SpecificationSerializers()
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    rating = serializers.SerializerMethodField()

    def get_images(self, obj: {images}) -> list[dict[str, Any]]:
        """Добавляем поле images и по обератной связи получаем все изображения данного продукта"""
        return [{'src': img.images.url, 'alt': img.images.name} for img in obj.images.all()]

    def get_reviews(self, obj: {reviews}) -> list[dict[str, Any]]:
        """Добавляем поле reviews и получаем необходимые данные"""
        return [{
            'author': review.author.username,
            # "email": review.author.profile.email,
            "text": review.text,
            "rate": review.rate,
            "date": review.date,
        }
            for review in obj.reviews.all()
        ]

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


class ReviewSerializers(serializers.ModelSerializer):
    """Сериализации данных из модели Review"""
    class Meta:
        model = Review
        fields = ['text', 'rate']

