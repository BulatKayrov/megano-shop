# Generated by Django 4.2.3 on 2023-07-19 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('deliveryType', models.CharField(choices=[('free', 'Free'), ('paid', 'Paid')], max_length=200)),
                ('paymentType', models.CharField(choices=[('online', 'Online'), ('cash', 'Cash')], max_length=200)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('accepted', 'Accepted'), ('processing', 'Processing'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], max_length=200)),
                ('city', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=256)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='profile_app.profile')),
                ('products', models.ManyToManyField(related_name='orders', to='product.products', verbose_name='продуты')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='orders.order', verbose_name='Адрес доставки')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
            options={
                'verbose_name': 'Продукт в заказе',
                'verbose_name_plural': 'Продукты в заказе',
            },
        ),
    ]
