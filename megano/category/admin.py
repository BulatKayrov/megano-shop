from django.contrib import admin
from .models import Category, Subcategory


class SubCategoryAdmon(admin.TabularInline):
    model = Subcategory
    extra = 1
    fieldsets = (
        (None, {
            # 'classes': ('collapse',),
            'fields': (('title', 'image'),)
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # fields = ('title', 'image')
    list_display = ("__str__",)
    inlines = [SubCategoryAdmon]
    fieldsets = (
        ('Категория', {
            'fields': (('title', 'image'),)
        }),
    )

