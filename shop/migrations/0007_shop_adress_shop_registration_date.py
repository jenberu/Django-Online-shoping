# Generated by Django 5.0.6 on 2024-06-17 17:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_category_shop_alter_product_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='adress',
            field=models.CharField(default='bahirdar', max_length=200),
        ),
        migrations.AddField(
            model_name='shop',
            name='registration_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
