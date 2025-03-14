# Generated by Django 5.0.6 on 2024-07-22 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('telegram_url', models.URLField(blank=True, null=True)),
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='social_media', to='shop.shop')),
            ],
        ),
    ]
