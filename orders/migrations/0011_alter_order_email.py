# Generated by Django 5.0.6 on 2024-10-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_remove_order_postal_code_order_house_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='e-mail'),
        ),
    ]
