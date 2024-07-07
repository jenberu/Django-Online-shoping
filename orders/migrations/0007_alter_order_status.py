# Generated by Django 5.0.6 on 2024-07-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('delivered', 'Delivered'), ('out of delivery', 'Out of Delivery'), ('confirmed', 'Order Confirmed')], default=('pending', 'Pending'), max_length=30),
        ),
    ]
